# formulario crear usuarios

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# para que no se rompa
User = get_user_model()

class RegistroForm(UserCreationForm):
    #agregamos telefono de user personalizado (es_agente no esta y por def false, solo admin en panel puede config esto))
    email = forms.EmailField(required=True, label="Correo Electrónico")
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    telefono = forms.CharField(required=False, label="Teléfono de Contacto")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono']

    # estilos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border-2 border-black rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all text-gray-900 bg-white'
            })