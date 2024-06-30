from django.shortcuts import render, redirect
from app.models import Course
from .forms import CheckForm
from student.models import Student

def student_cabinet(request):
    user = Student.objects.get(student_user=request.user)
    
    return render(request, 'student_cabinet.html', {'user':user})


def student_comment(request):
    return render(request, 'student_comment.html', {})

def join_course(request, pk):
    course = Course.objects.get(pk=pk)
    form = CheckForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.customer = request.user
        instance.course = course
        instance.save()
        return redirect('student:answer')
    return render(request, 'join_course.html', {'course': course, 'form': form})
    

def answer(request):
    return render(request, 'answer.html', {})
