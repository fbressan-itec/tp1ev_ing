from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import Propiedad, ImagenPropiedad, Cliente, Transaccion, Cita
from .forms import PropiedadForm, ClienteForm, CitaForm

# verificar if admin o agente 
def es_agente_o_admin(user):
    return user.is_authenticated and (user.is_staff or getattr(user, 'es_agente', False))

# logica traer lista de propiedades
@login_required
def lista_propiedades(request):
    # traer las propiedades de la bd
    propiedades = Propiedad.objects.all()
    # las paos al template inmobiliaria
    return render(request, 'inmobiliaria/lista.html', {'propiedades': propiedades})

# logica para "ver mas" detalles de cada propiedad por id
@login_required
@permission_required('inmobiliaria.view_propiedad', login_url='lista_propiedades')
def detalle_propiedad(request, pk):
    # get o 404 por id/pk
    propiedad = get_object_or_404(Propiedad, pk=pk)
    return render(request, 'inmobiliaria/detalle.html', {'propiedad': propiedad})

# logica formulario cargar propiedades CRUD
@login_required
#@user_passes_test(es_agente_o_admin, login_url='lista_propiedades')
@permission_required('inmobiliaria.add_propiedad', login_url='lista_propiedades')
def crear_propiedad(request):
    if request.method == 'POST':
        # .FILES para traer imagenes
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            propiedad = form.save(commit=False)
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
@login_required
#@user_passes_test(es_agente_o_admin, login_url='lista_propiedades')
@permission_required('inmobiliaria.change_propiedad', login_url='lista_propiedades')
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
@login_required
#@user_passes_test(es_agente_o_admin, login_url='lista_propiedades')
@permission_required('inmobiliaria.delete_propiedad', login_url='lista_propiedades')
def eliminar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        propiedad.delete() #borramos y cargamos bd
        return redirect('lista_propiedades')
    
    return render(request, 'inmobiliaria/confirmar_eliminar.html', {'propiedad': propiedad})

# para agregar home (publica)
def home(request):
    return render(request, 'home.html')

# lista de clientes
@login_required
@permission_required('inmobiliaria.view_cliente', login_url='lista_propiedades')
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'inmobiliaria/lista_clientes.html', {'clientes': clientes})

#Lista de transacciones
@login_required
@permission_required('inmobiliaria.view_transaccion', login_url='lista_propiedades')
def lista_transacciones(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'inmobiliaria/lista_transacciones.html', {'transacciones': transacciones})

#losta de citas
@login_required
@permission_required('inmobiliaria.view_cita', login_url='lista_propiedades')
def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'inmobiliaria/lista_citas.html', {'citas': citas})

# Agregar datos de posibles clientes
@login_required
@permission_required('inmobiliaria.add_cliente', login_url='lista_propiedades')
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'inmobiliaria/form_generico.html', {'form': form, 'titulo_pantalla': 'Registrar Nuevo Cliente'})

# Crear citas con agentes
@login_required
@permission_required('inmobiliaria.add_cita', login_url='lista_propiedades')
def crear_cita(request):
    propiedad_id = request.GET.get('propiedad_id') # Capturamos si viene desde una propiedad
    
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        initial_data = {}
        # traer del id q preciona el boton de citas
        if propiedad_id:
            initial_data['propiedad'] = get_object_or_404(Propiedad, pk=propiedad_id)
        form = CitaForm(initial=initial_data)
        
    return render(request, 'inmobiliaria/form_generico.html', {'form': form, 'titulo_pantalla': 'Agendar Nueva Cita / Visita'})

#editar cliente solo logueados
@login_required
@permission_required('inmobiliaria.change_cliente', login_url='lista_propiedades')
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'inmobiliaria/form_generico.html', {'form': form, 'titulo_pantalla': 'Editar Datos del Cliente'})

#eliminar clientes (NO LOGICO) solo usuario
@login_required
@permission_required('inmobiliaria.delete_cliente', login_url='lista_propiedades')
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'inmobiliaria/confirmar_eliminar_generico.html', {
        'objeto': cliente, 
        'nombre_objeto': f"al cliente {cliente.apellido}, {cliente.nombre}",
        'url_cancelar': 'lista_clientes'
    })

#editar cita (por ahora usuario)
@login_required
@permission_required('inmobiliaria.change_cita', login_url='lista_propiedades')
#@user_passes_test(es_agente_o_admin, login_url='lista_propiedades') #desmarcar si lo dejo solo admin
def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'inmobiliaria/form_generico.html', {'form': form, 'titulo_pantalla': 'Modificar Cita / Visita'})

#eliminar (NO LOGICO) cita (por ahora solo usuario)
@login_required
#@user_passes_test(es_agente_o_admin, login_url='lista_propiedades') #desmarcar si pongo solo admin
@permission_required('inmobiliaria.delete_cita', login_url='lista_propiedades')
def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('lista_citas')    
    #para que no se rompa
    fecha_formateada = cita.fecha_hora.strftime('%d/%m/%Y %H:%M')    
    return render(request, 'inmobiliaria/confirmar_eliminar_generico.html', {
        'objeto': cita, 
        'nombre_objeto': f"la cita programada para el {fecha_formateada} hs",
        'url_cancelar': 'lista_citas'
    })