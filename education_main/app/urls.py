from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('course1/', views.course1, name='course1'),
    path('course2/', views.course2, name='course2'),
    path('course3/', views.course3, name='course3')
]