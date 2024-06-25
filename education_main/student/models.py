from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_user = models.OneToOneField(User, on_delete=models.CASCADE)   
    course = models.ForeignKey('app.Course', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.student_user.username


class Check(models.Model):
    file = models.FileField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    course = models.ForeignKey('app.Course', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.customer.username} {self.date_created}'

