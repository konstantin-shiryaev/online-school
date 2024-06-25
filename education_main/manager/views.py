from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from student.models import Student, Check


# Create your views here.
def requests(request):
    feedbacks = Request.objects.all()
    return render(request, 'requests.html', {'feedbacks': feedbacks})


def manager_cabinet(request):
    users = User.objects.filter(groups__name="Студенты")
    teachers = User.objects.filter(groups__name="Преподаватели")
    students_objects = Student.objects.all()
    students = []

    for student in students_objects:
        students.append({
            'id': student.pk,
            'last_name': student.student_user.last_name,
            'first_name': student.student_user.first_name,
            'username': student.student_user.username,
            'email': student.student_user.email
        })

    context = {
        'title': 'Список студентов',
        'school': 'Академия программистов',
        'users': users,
        'teachers': teachers,
        'students': students
    }
    return render(request, 'manager_cabinet.html', context)


def deactivate_user(request, pk):
    user = User.objects.get(pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect("manager:manager_cabinet")



def user_checks(request):   
    checks = Check.objects.all()
    return render(request, 'user_checks.html', {'checks': checks})

