from django.shortcuts import render

# Create your views here.
def teacher_cabinet(request):
    context = {
        'title': 'Список студентов',
        'school': 'school'
    }
    return render(request, 'teacher_cabinet.html', context)
