from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def course1(request):
    return render(request, 'course-grid-1.html', {})

def course2(request):
    return render(request, 'course-grid-2.html', {})

def course3(request):
    return render(request, 'course-grid-3.html', {})

def about_us(request):
    return render(request, 'about.html', {})

def teachers(request):
    return render(request, 'teachers.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})
    
def contact(request):
    return render(request, 'contact.html', {})

# def book(request):
#     return render(request, 'teachers.html', {})

# ale
# ale 2
# ale 3
