from django.db import models
from django.conf import settings
from django.utils.formats import date_format # Importación segura para fechas

# model de los inmuebles
class Propiedad(models.Model):
    # tipo de inmueble
    TIPO_CHOICES = [
        ('CASA', 'Casa'),
        ('DEPA', 'Departamento'),
        ('TERR', 'Terreno'),
        ('LOCA', 'Local Comercial'),
    ]
    # estado/disponibilidad
    ESTADO_CHOICES = [
        ('DISP', 'Disponible'),
        ('ALQU', 'Alquilada'),
        ('VEND', 'Vendida'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    direccion = models.CharField(max_length=250, verbose_name="Dirección")
    precio = models.DecimalField(max_length=12, decimal_places=2, max_digits=12, verbose_name="Precio (USD)")
    tipo = models.CharField(max_length=4, choices=TIPO_CHOICES, default='CASA')
    estado = models.CharField(max_length=4, choices=ESTADO_CHOICES, default='DISP')
    agente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="propiedades")

    class Meta:
        verbose_name_plural = "Propiedades"
    def __str__(self):
        return f"{self.titulo} - {self.get_tipo_display()} (${self.precio})"

# model para las fotos de casas ImageField
class ImagenPropiedad(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name="imagenes")
    # van en carpeta 'propiedades' dentro de media
    imagen = models.ImageField(upload_to="propiedades/") 
    descripcion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Descripción de la foto")

    def __str__(self):
        return f"Foto de {self.propiedad.titulo}"

# model para los clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=15, unique=True, verbose_name="DNI")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo Electrónico")

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

# modelo para de contrato venta/alquiler
class Transaccion(models.Model):
    TIPO_OP_CHOICES = [
        ('VENTA', 'Venta'),
        ('ALQUILER', 'Alquiler'),
    ]
    propiedad = models.ForeignKey(Propiedad, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    agente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    tipo_operacion = models.CharField(max_length=10, choices=TIPO_OP_CHOICES)
    fecha = models.DateField(auto_now_add=True)
    monto_final = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name_plural = "Transacciones"

    def __str__(self):
        return f"{self.tipo_operacion} de {self.propiedad.titulo} - {self.fecha}"

# por si hago un turnero de citas para mostrar viviendas
class Cita(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(verbose_name="Fecha y Hora de la cita")
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        # solucion a crasheo si dejo vacio campo de fecha
        return f"Cita: {self.cliente} ve {self.propiedad.titulo} ({self.fecha_hora})"