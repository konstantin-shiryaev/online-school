from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import *


def log_in(request):
    form=LoginForm(data=request.POST or None)
    
    if form.is_valid():
        user=form.get_user()
        group = user.groups.all()[0].name.lower()
        redirects = {
            'менеджер': 'manager:manager_cabinet',
            'преподаватели': 'teacher:teacher_cabinet',
            'студенты': 'student:student_cabinet',
        }
        login(request,user)
        if user.is_superuser:
            return redirect('manager:manager_cabinet')
        return redirect(redirects[group])
    return render(request, 'index.html', {})

def log_out(request):
    if request.method == 'POST':
        logout(request)
    return redirect('app:index')
    
    