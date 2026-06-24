from django.urls import path
from . import views

#Rutas inmobiliaria/

urlpatterns = [
    path('', views.lista_propiedades, name='lista_propiedades'),
    path('propiedad/<int:pk>/', views.detalle_propiedad, name='detalle_propiedad'), #url de la propiedad por id/pk
    path('propiedad/nueva/', views.crear_propiedad, name='crear_propiedad'), #formulario cargar propiedades
    path('propiedad/<int:pk>/editar/', views.editar_propiedad, name='editar_propiedad'), #editar
    path('propiedad/<int:pk>/eliminar/', views.eliminar_propiedad, name='eliminar_propiedad'), #eliminar
]