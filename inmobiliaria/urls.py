from django.urls import path
from . import views

#Rutas inmobiliaria/

urlpatterns = [
    path('', views.lista_propiedades, name='lista_propiedades'),
    path('propiedad/<int:pk>/', views.detalle_propiedad, name='detalle_propiedad'), #url de la propiedad por id/pk
    path('propiedad/nueva/', views.crear_propiedad, name='crear_propiedad'), #formulario cargar propiedades
    path('propiedad/<int:pk>/editar/', views.editar_propiedad, name='editar_propiedad'), #editar
    path('propiedad/<int:pk>/eliminar/', views.eliminar_propiedad, name='eliminar_propiedad'), #eliminar

    path('transacciones/', views.lista_transacciones, name='lista_transacciones'),
    
    path('clientes/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),

    path('citas/', views.lista_citas, name='lista_citas'),
    path('citas/nueva/', views.crear_cita, name='crear_cita'),
    path('citas/<int:pk>/editar/', views.editar_cita, name='editar_cita'),
    path('citas/<int:pk>/eliminar/', views.eliminar_cita, name='eliminar_cita'),
]