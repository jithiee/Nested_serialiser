from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Teacher,Student
from . serializer import TeacherSerializer , StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.


class TeacherViewset(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   
class StudentVieewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]