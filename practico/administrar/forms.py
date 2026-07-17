from django import forms
from .models import Contacto
import re

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'telefono']
        error_messages = {
            'nombre': {
                'required': 'Por favor, ingresa el nombre completo del contacto.',
            },
            'correo': {
                'required': 'El correo electrónico es obligatorio.',
                'invalid': 'Por favor, ingresa una dirección de correo electrónico válida (ejemplo@correo.com).',
            },
            'telefono': {
                'required': 'El número de teléfono es obligatorio.',
            }
        }

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        
        if re.search(r'[a-zA-Z]', telefono):
            raise forms.ValidationError('El número de teléfono no puede contener letras. Ingresa solo números.')
            
        return telefono