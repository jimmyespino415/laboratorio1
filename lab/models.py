from django.db import models
from django.utils import timezone

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    direccion = models.TextField()
    ingreso_sistema = models.DateTimeField(
            default=timezone.now)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()