from django.db import models

# Create your models here.
class Teacher(models.Model):
     teacher_name = models.CharField( max_length=50)
     subject = models.CharField( max_length=50)
     
     def __str__(self):
          return self.teacher_name
     
    
        
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll  = models.IntegerField()
    city = models.CharField( max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name='studentdetiles') 
    
    