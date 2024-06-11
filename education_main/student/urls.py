from django.urls import path
from . import views
urlpatterns = [
    path('student_cabinet', views.student_cabinet, name='student_cabinet'),
]