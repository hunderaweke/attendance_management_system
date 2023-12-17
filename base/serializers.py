from .models import *
from rest_framework import serializers


class SimpleStudentSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()

    class Meta:
        model = Student
        fields = ["name", "email"]


class AttendanceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    student = SimpleStudentSerializer()

    class Meta:
        model = Attendance
        fields = ["id", "status", "student"]


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    student_attendance = AttendanceSerializer(read_only=True, many=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "email",
            "codeforces_handle",
            "student_attendance",
        ]


class EventSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    event_attendance = AttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ["id", "name", "starting_time", "ending_time", "event_attendance"]
