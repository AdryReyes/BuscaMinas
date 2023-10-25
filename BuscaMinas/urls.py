from django.urls import path
from BuscaMinas import views
from django.contrib import admin

urlpatterns = [
    path('', views.indexed, name='index'),
    path('crea_tablero/', views.crea_tablero, name='crea_tablero'),
]