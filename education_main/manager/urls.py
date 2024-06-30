from django.urls import path
from . import views

urlpatterns = [
    path('requests/', views.requests, name='requests'),
    path('manager_cabinet/', views.manager_cabinet, name='manager_cabinet'),
    path('teachers_table/', views.teachers_table, name='teachers_table'),
    path('students_table/', views.students_table, name='students_table'),
    path('deactivate_user/<int:pk>', views.deactivate_user, name='deactivate_user'),
    path('user_checks/', views.user_checks, name='user_checks'),
    path('add_student/', views.add_student, name='add_student'),
    path('read_request/<int:pk>', views.read_request, name='read_request'),
    path('archive_check/<int:pk>', views.archive_check, name='archive_check'),
]
