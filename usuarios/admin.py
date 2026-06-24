from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    # al admin de django le agrego tel y el bollean esagente
    fieldsets = UserAdmin.fieldsets + (
        ('Información Inmobiliaria', {'fields': ('telefono', 'es_agente')}),
    )