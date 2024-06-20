from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserQuestionForm
from .models import UserQuestion

# Create your views here.
def student_cabinet(request):
    # response = render_to_string('app/')
    return render(request, 'student_cabinet.html', {})


def student_comment(request):
    return render(request, 'student_comment.html', {})

def leaveAquestion(request):
    data = UserQuestion.objects.all()
    print(request.GET)
    if request.method == 'POST':
        form = UserQuestionForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('manager:requests')
    else:
        form = UserQuestionForm()
    return render(request, 'contact.html', {'form':form, 'data': data})