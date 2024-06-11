from django.urls import path
from . import views

urlpatterns = [
    path('requests', views.requests, name='requests'),
    path('manager_cabinet', views.manager_cabinet, name='manager_cabinet'),
    
]