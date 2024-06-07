from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
# from django.template.loader import render_to_string

# Create your views here.
school = 'Академия программистов'
def index(request):
    context = {
        'title': 'Главная страница',
        'school': school
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
    context = {
        'title': 'Наши преподаватели',
        'school': school
    }
    return render(request, 'teachers.html', context)

def pricing(request):
    context = {
        'title': 'Стоимость курсов',
        'school': school
    }
    return render(request, 'pricing.html', context)
    
def contact(request):
    context = {
        'title': 'Обратная связь',
        'school': school
    }
    # response = render_to_string('app/')
    return render(request, 'contact.html', context)

def order(request):
    # response = render_to_string('app/')
    return render(request, 'order.html', {})
def order2(request):
    # response = render_to_string('app/')
    return render(request, 'order2.html', {})
def student(request):
    # response = render_to_string('app/')
    return render(request, 'student.html', {})
def teachertable(request):
    context = {
        'title': 'Список студентов',
        'school': school
    }
    return render(request, 'teachertable.html', context)
