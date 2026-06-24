from django.contrib import admin
from .models import Propiedad, ImagenPropiedad, Cliente, Transaccion, Cita

# cargar imágenesdentro de la pantalla de la Propiedad
class ImagenPropiedadInline(admin.TabularInline):
    model = ImagenPropiedad
    extra = 1  # carga una imagen por def

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'precio', 'estado', 'agente') # columnas en la lista db
    list_filter = ('tipo', 'estado') # filtrar x tipo y estado
    search_fields = ('titulo', 'direccion', 'descripcion') # barra de búsqueda
    ordering = ('precio',) # ordenar por def precio
    inlines = [ImagenPropiedadInline] 

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'telefono', 'email')
    search_fields = ('apellido', 'nombre', 'dni')
    ordering = ('apellido', 'nombre') #ordena primer apellido desp nombre

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('propiedad', 'cliente', 'tipo_operacion', 'fecha', 'monto_final')
    list_filter = ('tipo_operacion', 'fecha')
    search_fields = ('propiedad__titulo', 'cliente__apellido') # busqueda por casa o cliente
    ordering = ('-fecha',) # orden x fecha

@admin.register(Cita)
# para las citas/consultas
class CitaAdmin(admin.ModelAdmin):
    list_display = ('propiedad', 'cliente', 'fecha_hora')
    list_filter = ('fecha_hora',)
    ordering = ('fecha_hora',)