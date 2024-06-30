from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from student.models import Student, Check
from app.models import Course
from teacher.models import Teacher
# Create your views here.
def requests(request):
    feedbacks = Request.objects.all()
    return render(request, 'requests.html', {'feedbacks': feedbacks})


def manager_cabinet(request):
    users = User.objects.filter(groups__name="Студенты")

    

    context = {
        'title': 'Список студентов',
        'school': 'Академия программистов',
        'users': users,
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
    checks = Check.objects.filter(confirmed=True) if request.GET.get('confirmed') else Check.objects.filter(confirmed=False)
    
    return render(request, 'user_checks.html', {'checks': checks})

def add_student(request):
    user = User.objects.get(pk=request.GET.get('user'))
    course = Course.objects.get(pk=request.GET.get('course'))
    

    if request.method == 'POST':
        Student.objects.filter(student_user=user).update(course=course)
        Check.objects.filter(customer=user, course=course).update(confirmed=True)
        return redirect('manager:manager_cabinet')
    context = {'user': user, 'course':course}
    return render(request, 'confirm_student_creation.html', context)

def teachers_table(request):
    teachers_objects = Teacher.objects.all()
    teachers = []

    for teacher in teachers_objects:
        teachers.append({
            'id': teacher.pk,
            'last_name': teacher.teacher_user.last_name,
            'first_name': teacher.teacher_user.first_name,
            'username': teacher.teacher_user.username,
            'email': teacher.teacher_user.email,
            'date_joined':teacher.teacher_user.date_joined
        })
    return render(request, 'teachers_table.html', {'teachers':teachers})

def students_table(request):
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
    return render(request, 'students_table.html', {'students':students})

def read_request(request, pk):
    request_object = Request.objects.get(pk=pk)

    
    request_object.is_accepted = True
    request_object.save()
    return redirect('manager:requests')

def archive_check(request,pk):
    check = Check.objects.get(pk=pk)
    check.confirmed = True
    check.save()
    return redirect('manager:user_checks')

