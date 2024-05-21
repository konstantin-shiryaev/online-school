from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us')
]