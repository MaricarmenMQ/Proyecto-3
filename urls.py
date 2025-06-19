
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hola, name="index"),
    path("datos", views.datos_personales, name="datos"),
    path("preferencias", views.preferencias, name="preferencias"),
    path("gustos", views.gustos, name="gustos"),
    path("habilidades", views.habilidades, name="habilidades"),
    path("familia", views.familia, name="familia"),
    
]

