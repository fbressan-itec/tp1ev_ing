from django import forms
from .models import Propiedad, Cliente, Cita

class PropiedadForm(forms.ModelForm):
    # Agregamos un campo manual para la imagen principal de la propiedad
    imagen_principal = forms.ImageField(required=False, label="Foto de la Propiedad")

    class Meta:
        model = Propiedad
        # campos a rellenar
        fields = ['titulo', 'descripcion', 'direccion', 'precio', 'tipo', 'estado']
        
    # agregar front rapido
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all'
            })

# formularios para clientes
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'dni', 'telefono', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full p-2.5 rounded-xl border-2 border-black focus:outline-none focus:border-blue-600 bg-white text-gray-900'})

#   formulario para citas (control de campos a completar)
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['propiedad', 'cliente', 'fecha_hora', 'comentarios']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'comentarios': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full p-2.5 rounded-xl border-2 border-black focus:outline-none focus:border-blue-600 bg-white text-gray-900'})