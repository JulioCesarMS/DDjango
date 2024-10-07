from django.contrib import admin
from django.urls import path, include
from gestion_libros import views as gestion_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gestion_views.registro_usuario, name='inicio'),  # Redirige la raíz a la vista de lista de libros
    path('gestion_libros/', include('gestion_libros.urls')),  # Enlaza las rutas de la app gestion_libros
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación (login, logout, password change)
]