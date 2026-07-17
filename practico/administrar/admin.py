from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'telefono', 'fecha_creacion')
    search_fields = ('nombre', 'correo', 'telefono')
    list_filter = ('fecha_creacion',)
