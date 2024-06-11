from django.shortcuts import render

# Create your views here.
def student_cabinet(request):
    # response = render_to_string('app/')
    return render(request, 'student_cabinet.html', {})