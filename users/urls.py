from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_user, name='new_user'),
    path('users/login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]