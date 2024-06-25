from django.urls import path
from . import views

urlpatterns = [
    path('requests', views.requests, name='requests'),
    path('manager_cabinet', views.manager_cabinet, name='manager_cabinet'),
    path('deactivate_user/<int:pk>', views.deactivate_user, name='deactivate_user'),
    path('user_checks', views.user_checks, name='user_checks'),
]
