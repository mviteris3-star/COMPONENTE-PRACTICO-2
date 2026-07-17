from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editar/<int:pk>/', views.editar_contacto, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_contacto, name='eliminar'),
]