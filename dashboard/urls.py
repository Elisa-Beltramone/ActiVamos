from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('agenda/', views.activities, name='activities')
]