from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(_('nombre'), max_length=50)
    apellido = models.CharField(_('apellido'), max_length=50)
    edad = models.IntegerField(_('edad'))
    direccion = models.TextField(_('direccion'))
    ingreso_sistema = models.DateTimeField(_('ingreso_sistema'),
            default=timezone.now)
    telefono = models.CharField(_('telefono'), help_text'Formato 0212-1234567', max_length=12)
    email = models.EmailField(_('email'))