from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    teacher_user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='author.jpg')

    def __str__(self):
        return self.teacher_user.username
