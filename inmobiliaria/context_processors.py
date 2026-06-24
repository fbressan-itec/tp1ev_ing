from .models import Propiedad

def datos_inmobiliaria(request):
    # VER de usar el contador y los datos para footer
    return {
        'global_nombre_web': 'InmoMint',
        'global_telefono': '+54 9 358 5111111',
        'global_email': 'contacto@inmomint.com',
        'global_total_propiedades': Propiedad.objects.count()
    }