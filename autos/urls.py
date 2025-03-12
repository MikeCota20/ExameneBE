from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar, name='agregar'),
    path('', views.registrados, name='registrados'),
]