from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contacto
from .forms import ContactoForm
def index(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        contactos = Contacto.objects.filter(nombre__icontains=query)
    else:
        contactos = Contacto.objects.all()
    es_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    
    if es_ajax:
        return render(request, 'administrar/contactos_list.html', {'contactos': contactos})

    if request.method == 'POST':
        form = ContactoForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = ContactoForm() 
    return render(request, 'administrar/index.html', {
        'form': form,
        'contactos': contactos,
        'editando': False
    })

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

def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('index')