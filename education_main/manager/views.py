from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def requests(request):
    # response = render_to_string('app/')
    return render(request, 'requests.html', {})
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


def delete_student(request, pk):
    students = User.objects.get(pk=pk)
    if request.method == 'POST':
        
        students.delete()
        return redirect('manager:manager_cabinet')
    return render(request, "manager_cabinet.html")