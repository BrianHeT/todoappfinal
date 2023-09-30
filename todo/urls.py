from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetRoutes, name='routes'),
    path('todo/', views.getTodo, name="tareas"),
    
]