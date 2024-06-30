from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import *
from .utils import redirects
from django.contrib.auth.models import Group
from teacher.models import Teacher
from student.models import Student
def log_in(request):
    form = LoginForm(data=request.POST or None)
    
    if form.is_valid():
        user = form.get_user()
        group = user.groups.all()[0].name.lower()

        
        login(request, user)
        if user.is_superuser:
            return redirect('manager:manager_cabinet')
        return redirect(redirects[group])
    return render(request, 'index.html', {})


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        if request.user.is_authenticated and request.user.groups.all()[0].name == 'Менеджер':
            teachers = Group.objects.get(name='Преподаватели')
            teachers.user_set.add(user)
            Teacher.objects.create(teacher_user=user)
            return redirect('manager:manager_cabinet')
        else:
            students = Group.objects.get(name='Студенты')
            students.user_set.add(user)
            login(request, user)
            Student.objects.create(student_user=user)
            return redirect('app:pricing')
    return render(request, 'index.html')


def log_out(request):
    if request.method == 'POST':
        logout(request)
    return redirect('app:index')