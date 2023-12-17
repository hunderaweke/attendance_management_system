from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    codeforces_handle = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    starting_time = models.DateField()
    ending_time = models.DateField()

    def __str__(self) -> str:
        return self.name


class Attendance(models.Model):
    event = models.ForeignKey(
        to="Event", related_name="attendance_event", on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        to="student", related_name="attendee", on_delete=models.PROTECT
    )
    ATTENDANCE_CHOICES = [
        ("P", "Present"),
        ("A", "Absent"),
        ("E", "Excused"),
    ]
    status = models.CharField(max_length=25, choices=ATTENDANCE_CHOICES, default="A")

    def __str__(self) -> str:
        return (
            f"Attendance for {self.event} - {self.event.starting_time}- {self.student}"
        )


@receiver(post_save, sender=Event)
def create_attendance(sender, instance, **kwargs):
    for student in Student.objects.all():
        attendance = Attendance.objects.create(event=instance, student=student)


@receiver(post_save, sender=Student)
def create_attendance(sender, instance, **kwargs):
    for event in Event.objects.all():
        attendance = Attendance.objects.create(event=event, student=instance)
