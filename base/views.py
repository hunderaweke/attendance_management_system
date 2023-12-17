from .serializers import *
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        if "student_pk" in self.kwargs:
            return Attendance.objects.filter(student_id=self.kwargs["student_pk"])
        return Attendance.objects.filter(student_id=self.kwargs["event_pk"])


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
