
from django.shortcuts import render
from app.models import Course
from .models import Teacher
from student.models import Student
from django.db.models import Subquery, OuterRef
# Create your views here.
def teacher_cabinet(request):
    teacher = Teacher.objects.get(teacher_user=request.user)

    students = Student.objects.annotate(
        teacher_id=Subquery(
            Course.objects.filter(
                teacher=OuterRef('course__teacher')
            ).values('teacher')[:1]
        )
    ).filter(teacher_id=teacher.id).distinct()

    context = {
        'title': 'Список студентов',
        'school': 'Академия программистов',
        'students': students
    }
    return render(request, 'teacher_cabinet.html', context)