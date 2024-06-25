from django.db import models

# Create your models here.

class Request(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.body
     