from django import forms
from .models import Propiedad

class PropiedadForm(forms.ModelForm):
    # Agregamos un campo manual para la imagen principal de la propiedad
    imagen_principal = forms.ImageField(required=False, label="Foto de la Propiedad")

    class Meta:
        model = Propiedad
        # campos a rellenar
        fields = ['titulo', 'descripcion', 'direccion', 'precio', 'tipo', 'estado']
        
    # agregar tailwind
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all'
            })