from django.shortcuts import render

# Create your views here.
def requests(request):
    # response = render_to_string('app/')
    return render(request, 'requests.html', {})
def manager_cabinet(request):
    # response = render_to_string('app/')
    return render(request, 'manager_cabinet.html', {})