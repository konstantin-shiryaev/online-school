from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def teacher_cabinet(request):
    students = User.objects.filter(groups__name="Студенты")
    context = {
        'title': 'Список студентов',
        'school': 'school',
        'students': students
    }
    return render(request, 'teacher_cabinet.html', context)
