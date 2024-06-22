from django.shortcuts import render
from app.models import Course

def student_cabinet(request):
    # response = render_to_string('app/')
    return render(request, 'student_cabinet.html', {})


def student_comment(request):
    return render(request, 'student_comment.html', {})

def join_course(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'join_course.html', {'course': course})