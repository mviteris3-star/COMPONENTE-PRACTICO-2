from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contacto
from .forms import ContactoForm

# 1. VISTA PRINCIPAL CON BÚSQUEDA AJAX
# 1. VISTA PRINCIPAL CON BÚSQUEDA AJAX (Corregida de UnboundLocalError)
# 1. VISTA PRINCIPAL CON BÚSQUEDA AJAX (Corregida para retener errores)
def index(request):
    query = request.GET.get('q', '').strip()
    
    # Búsqueda normal de contactos
    if query:
        contactos = Contacto.objects.filter(nombre__icontains=query)
    else:
        contactos = Contacto.objects.all()

    # Detectar petición AJAX (Búsqueda en tiempo real)
    es_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    
    if es_ajax:
        return render(request, 'administrar/contactos_list.html', {'contactos': contactos})

    # PROCESAR EL FORMULARIO
    if request.method == 'POST':
        form = ContactoForm(request.POST) # Cargamos los datos del usuario
        if form.is_valid():
            form.save()
            return redirect('index') # Si es válido, guardamos y limpiamos
        # IMPORTANTE: Si NO es válido, NO entramos al 'else'. 
        # Dejamos que la variable 'form' conserve los errores y los datos ingresados.
    else:
        form = ContactoForm() # Solo creamos un formulario limpio para peticiones GET normales
        
    # Renderizamos la página pasando la variable 'form' (que si falló la validación, tiene los errores dentro)
    return render(request, 'administrar/index.html', {
        'form': form,
        'contactos': contactos,
        'editando': False
    })

# 2. VISTA PARA EDITAR CONTACTO
def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactoForm(instance=contacto)
    
    contactos = Contacto.objects.all()
    return render(request, 'administrar/index.html', {
        'form': form,
        'contactos': contactos,
        'editando': True
    })

# 3. VISTA PARA ELIMINAR CONTACTO
def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('index')