from django.urls import path
from . import views

#Rutas inmobiliaria/

urlpatterns = [
    path('', views.lista_propiedades, name='lista_propiedades'),
    path('propiedad/<int:pk>/', views.detalle_propiedad, name='detalle_propiedad'), #url de la propiedad por id/pk
]