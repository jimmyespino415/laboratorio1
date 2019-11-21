from django import forms
from .models import Persona
from django.utils.translation import ugettext_lazy as _

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('nombre', 'apellido','edad','direccion', 'telefono','email')