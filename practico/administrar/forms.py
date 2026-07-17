from django import forms
from .models import Contacto
import re

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'telefono']
        # Definimos los mensajes de error amigables para campos vacíos o correos inválidos
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

    # Validación personalizada para el teléfono (que no tenga letras)
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        
        # Expresión regular: busca si hay alguna letra (a-z o A-Z)
        if re.search(r'[a-zA-Z]', telefono):
            raise forms.ValidationError('El número de teléfono no puede contener letras. Ingresa solo números.')
            
        return telefono