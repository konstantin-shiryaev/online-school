from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def requests(request):
    feedbacks = Request.objects.all()
    return render(request, 'requests.html', {'feedbacks': feedbacks})


def manager_cabinet(request):
    # response = render_to_string('app/')
    students = User.objects.filter(groups__name="Студенты")
    teachers = User.objects.filter(groups__name="Преподаватели")
    context = {
        'title': 'Список студентов',
        'school': 'school',
        'students': students,
        'teachers': teachers
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


