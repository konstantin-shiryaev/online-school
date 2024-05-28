from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model): # tr = teacher
    fullname_tr = models.CharField(max_length=255) # tr = teacher
    mail_tr = models.CharField(max_length=255)  # tr = teacher
    birthday_tr = models.DateField() # tr = teacher
    datecreated_tr = models.DateField(auto_now_add=True) # tr = teacher
    def __str__(self):
        return self.fullname_tr
    

class Student(models.Model): # st = student
    fullname_st = models.CharField(max_length=255) # st = student
    mail_st = models.CharField(max_length=255)  # st = student
    birthday_st = models.DateField() # st = student
    datecreated_st = models.DateField(auto_now_add=True) # st = student
    def __str__(self):
        return self.fullname_st
    
class Course(models.Model):
    name_course = models.CharField(max_length=255)
    price_course = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='likes')
    slug = models.SlugField(unique=True)
    students = models.ManyToManyField('app.Student')
    teachers = models.ManyToManyField('app.Teacher')
    def __str__(self):
        return self.name_course    
    