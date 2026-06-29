# formulario crear usuarios

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class RegistroForm(UserCreationForm):
    # Definimos los campos para agregarles la clase CSS y hacer obligatorios los que hagan falta
    email = forms.EmailField(required=True, label="Correo Electrónico", widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(required=False, label="Teléfono de Contacto", widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
        # Heredamos los campos base (username y contraseñas) y les acoplamos los tuyos
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'telefono')

    # estilos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border-2 border-black rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all text-gray-900 bg-white'
            })