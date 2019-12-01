from django import forms
from .models import Persona
from django.utils.translation import ugettext_lazy as _

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('nombre', 'apellido','edad','direccion', 'telefono','email')

    def clean_edad(self):
        data = self.cleaned_data['edad']
        if data < 1:
            raise forms.ValidationError("Edad tiene que ser un valor positivo")
        return data
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono.find("-") >= 0:
            x = telefono.split("-")
            if len(x[0])!=4 or not x[0].isdigit() or len(x[1])!=7 or not x[1].isdigit():
                raise forms.ValidationError("Ingreso un error en el formato")
        else:
            raise forms.ValidationError("Debe seguir el formato indicado")
        return telefono
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not nombre.isalpha():
            raise forms.ValidationError("El nombre debe estar formado por letras")
        return nombre 

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if not apellido.isalpha():
            raise forms.ValidationError("El apellido debe estar formado por letras")
        return apellido
