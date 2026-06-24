from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

#logica registrar usuario
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save() # actualizo bd
            login(request, user)
            return redirect('lista_propiedades')
    else:
        form = RegistroForm()
        
    # ruta actualizada a usuarios/registro        ***OK***
    return render(request, 'usuarios/registro.html', {'form': form})

