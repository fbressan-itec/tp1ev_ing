from django.shortcuts import render, get_object_or_404, redirect
from .models import Propiedad, ImagenPropiedad
from .forms import PropiedadForm

# logica traer lista de propiedades
def lista_propiedades(request):
    # traer las propiedades de la bd
    propiedades = Propiedad.objects.all()
    # las paos al template inmobiliaria
    return render(request, 'inmobiliaria/lista.html', {'propiedades': propiedades})

# logica para "ver mas" detalles de cada propiedad por id
def detalle_propiedad(request, pk):
    # get o 404 por id/pk
    propiedad = get_object_or_404(Propiedad, pk=pk)
    return render(request, 'inmobiliaria/detalle.html', {'propiedad': propiedad})

# logica formulario cargar propiedades CRUD
def crear_propiedad(request):
    if request.method == 'POST':
        # .FILES para traer imagenes
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            propiedad = form.save(commit=False)
            # si esta logueado le asigna ese user automatico
            if request.user.is_authenticated:
                propiedad.agente = request.user
            propiedad.save() # subimos a la db

            # subimos y vinculamos la imagen
            imagen_archivo = request.FILES.get('imagen_principal')
            if imagen_archivo:
                ImagenPropiedad.objects.create(propiedad=propiedad, imagen=imagen_archivo)

            return redirect('lista_propiedades')
    else:
        form = PropiedadForm()
    
    return render(request, 'inmobiliaria/form_propiedad.html', {'form': form, 'titulo_pantalla': 'Publicar Nueva Propiedad'})

# logica para editar CRUD
def editar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES, instance=propiedad)
        if form.is_valid():
            propiedad = form.save() #cargamos la edicion abd
            
            # fotos (carga una nueva, no remplaza la vieja)
            imagen_archivo = request.FILES.get('imagen_principal')
            if imagen_archivo:
                ImagenPropiedad.objects.create(propiedad=propiedad, imagen=imagen_archivo)
            # fotos editar foto existente
            """
            if imagen_archivo:
                # traigo la foto vieja
                foto_vieja = propiedad.imagenes.first()
                if foto_vieja:
                    foto_vieja.imagen = imagen_archivo
                    foto_vieja.save()
                else:
                    ImagenPropiedad.objects.create(propiedad=propiedad, imagen=imagen_archivo)
            """
                
            return redirect('detalle_propiedad', pk=propiedad.pk)
    else:
        # cargar el form actualizado
        form = PropiedadForm(instance=propiedad)
    
    return render(request, 'inmobiliaria/form_propiedad.html', {'form': form, 'titulo_pantalla': 'Editar Propiedad'})

# logica eliminar CRUD (borrado directo, ver de modificar model e implementar borrado logico)
def eliminar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        propiedad.delete() #borramos y cargamos bd
        return redirect('lista_propiedades')
    
    return render(request, 'inmobiliaria/confirmar_eliminar.html', {'propiedad': propiedad})