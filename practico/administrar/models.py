from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre completo")
    correo = models.EmailField(unique=True, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Número telefónico")
    
    # Campos opcionales pero muy útiles para una agenda real:
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['nombre']
