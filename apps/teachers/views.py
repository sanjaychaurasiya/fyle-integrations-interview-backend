from rest_framework import generics, status
from rest_framework.response import Response
from .models import Teacher
from apps.students.models import Assignment
# from apps.students.models import Student
from .serializers import TeacherAssignmentSerializer


# Create your views here.
class TeacherView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = TeacherAssignmentSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = TeacherAssignmentSerializer
