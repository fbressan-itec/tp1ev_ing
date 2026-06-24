from django.urls import path
from . import views

#Rutas inmobiliaria/

urlpatterns = [
    path('', views.lista_propiedades, name='lista_propiedades'),
]