from rest_framework import serializers
from . models import Teacher, Student

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id','name','roll','city','teacher']
        
class TeacherSerializer(serializers.ModelSerializer):
    studentdetiles = StudentSerializer(many=True , read_only=True)
    class Meta:
        model = Teacher
        fields = ['teacher_name','subject','studentdetiles']
        
# class customStudent(serializers.ModelSerializer):
    
#     class Meta:
#         model = Student
#         fields = ['id','name','roll','city','teacher','teacherdetails']
        
                
 
        
        
    