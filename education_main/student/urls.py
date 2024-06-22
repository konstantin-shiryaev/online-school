from django.urls import path
from . import views
urlpatterns = [
    path('student_cabinet', views.student_cabinet, name='student_cabinet'),
    path('student_comment', views.student_comment, name='student_comment'),
    path('join_course/<int:pk>', views.join_course, name='join_course'),
]