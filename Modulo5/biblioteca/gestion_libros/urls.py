from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
    path('nuevo/', views.nuevo_libro, name='nuevo_libro'),  # Registrar un nuevo libro
    path('lista/', views.lista_libros, name='lista_libros'),  # Listar todos los libros del usuario autenticado
    path('detalle/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),  # Ver detalles de un libro
    path('editar/<int:libro_id>/', views.editar_libro, name='editar_libro'),  # Editar un libro existente
    path('eliminar/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),  # Confirmar y eliminar un libro
]
