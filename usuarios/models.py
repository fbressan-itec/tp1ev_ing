from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    # Podés agregar un rol para saber si es Cliente o Agente Inmobiliario
    es_agente = models.BooleanField(default=False)

    def __str__(self):
        return self.username