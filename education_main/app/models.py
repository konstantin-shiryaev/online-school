from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.body
    

class Course(models.Model):
    teacher = models.ManyToManyField('teacher.Teacher', blank=True)
    title = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField()
    description = models.TextField()
    duration = models.PositiveSmallIntegerField()
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return self.title