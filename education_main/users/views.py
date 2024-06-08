from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import *


def log_in(request):
    form=LoginForm(data=request.POST or None)
    print(form.is_valid())
    if form.is_valid():
        user=form.get_user()
        login(request,user)
        print(user)
        return redirect('app:contact')
    return render(request, 'index.html', {})

def log_out(request):
    if request.method == 'POST':
        logout(request)
    return redirect('app:index')
    
    