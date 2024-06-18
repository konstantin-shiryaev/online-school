from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def student_cabinet(request):
    # response = render_to_string('app/')
    return render(request, 'student_cabinet.html', {})

