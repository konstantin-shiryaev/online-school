from django.shortcuts import render, redirect
from .forms import CommentForm, RequestForm
from .models import Review, Course
from teacher.models import Teacher
from users.utils import redirects

school = 'Академия программистов'
def index(request):
    reviews = Review.objects.all()
    context = {
        'title': 'Главная страница',
        'school': school,
        'reviews': reviews
    }
    return render(request, 'index.html', context)

def course1(request):
    context = {
        'title': 'Backend-разработчик',
        'school': school
    }
    return render(request, 'course-grid-1.html', context)

def course2(request):
    context = {
        'title': 'Frontend-разработчик',
        'school': school
    }
    return render(request, 'course-grid-2.html', context)

def course3(request):
    context = {
        'title': 'Fullstack-разработчик',
        'school': school
    }
    return render(request, 'course-grid-3.html', context)

def about_us(request):
    context = {
        'title': 'О нас',
        'school': school
    }
    return render(request, 'about.html', context)

def teachers(request):
    teachers = Teacher.objects.all()
    context = {
        'title': 'Наши преподаватели',
        'school': school,
        'teachers': teachers
        }
    return render(request, 'teachers.html', context)

def pricing(request):
    courses = Course.objects.all()
    context = {
        'title': 'Стоимость курсов',
        'school': school,
        'courses': courses
    }
    return render(request, 'pricing.html', context)
    
def contact(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:contact')
    else:
        form = RequestForm()
    return render(request, 'contact.html',  {'form': form})

def leave_review(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('student:student_cabinet')
    else:
        form = CommentForm()
    return render(request, 'student_comment.html', {'form':form})

def my_cabinet(request):
    if request.user.is_superuser:
        return redirect('manager:manager_cabinet')
    user_group = request.user.groups.all()[0].name.lower()
    
    return redirect(redirects[user_group])

