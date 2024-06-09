from django.urls import path
from . import views
urlpatterns = [
    path('teacher_cabinet', views.teacher_cabinet, name='teacher_cabinet'),
]