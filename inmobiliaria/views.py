from django.shortcuts import render
from .models import Propiedad

def lista_propiedades(request):
    # traer las propiedades de la bd
    propiedades = Propiedad.objects.all()
    # las paos al template inmobiliaria
    return render(request, 'inmobiliaria/lista.html', {'propiedades': propiedades})