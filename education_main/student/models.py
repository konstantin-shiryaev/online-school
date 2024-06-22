from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    student_user = models.OneToOneField(User, on_delete=models.CASCADE)   
    course = models.ForeignKey('app.Course', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.student_user.username
