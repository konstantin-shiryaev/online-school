from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('course1', views.course1, name='course1'),
    path('course2', views.course2, name='course2'),
    path('course3', views.course3, name='course3'),
    path('teachers', views.teachers, name='teachers'),
    path('pricing', views.pricing, name='pricing'),
    path('contact', views.contact, name='contact'),
    path('leave_review/', views.leave_review, name='leave_review')
    
    

]