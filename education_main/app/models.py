from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model): # tr = teacher
    firstname_tr = models.CharField(max_length=255) # tr = teacher
    surname_tr = models.CharField(max_length=255) # tr = teacher
    patronymic_tr = models.CharField(max_length=255) # tr = teacher
    mail_tr = models.EmailField()  # tr = teacher
    birthday_tr = models.DateField() # tr = teacher
    date_created_account_tr = models.DateField(auto_now_add=True) # tr = teacher
    conducting_courses_tr = models.ManyToManyField() # tr = teacher
    slug = models.SlugField(unique=True)
    """ss
    slug учителя. Нужен или нет? 
    """

class Students(models.Model): # st = student
    firstname_st = models.CharField(max_length=255) # st = student
    surname_st = models.CharField(max_length=255) # st = student
    patronymic_st = models.CharField(max_length=255) # st = student
    mail_st = models.EmailField()  # st = student
    date_created_account_st = models.DateField(auto_now_add=True) # st = student
    part_courses_st = models.ManyToManyField() # st = student
    
class Courses(models.Model):
    name_course = models.CharField(max_length=255)
    price_course = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='likes')
    views = models.ManyToManyField(User, related_name='views_quantity')
    