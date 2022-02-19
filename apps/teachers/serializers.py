from rest_framework import serializers
from .models import Teacher
# from apps.internal.models import User
from apps.students.models import Assignment


class TeacherAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"
