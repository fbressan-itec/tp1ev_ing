from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Inmobiliaria', {'fields': ('telefono', 'es_agente')}),
    )
    
    list_display = ['username', 'email', 'first_name', 'last_name', 'es_agente', 'is_staff']
    list_editable = ['es_agente']