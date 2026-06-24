from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Propiedad

# lista de propiedades
def lista_propiedades(request):
    # traer las propiedades de la bd
    propiedades = Propiedad.objects.all()
    # las paos al template inmobiliaria
    return render(request, 'inmobiliaria/lista.html', {'propiedades': propiedades})

# "ver mas" detalles de cada propiedad
def detalle_propiedad(request, pk):
    # get o 404 por id/pk
    propiedad = get_object_or_404(Propiedad, pk=pk)
    return render(request, 'inmobiliaria/detalle.html', {'propiedad': propiedad})