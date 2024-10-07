from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Libro, Categoria, Estado
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LibroForm, RegistroUsuarioForm


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  
            return redirect('lista_libros')  
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'gestion_libros/registro_usuario.html', {'form': form})

# Vista para registro de nuevos usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_libros')
    else:
        form = UserCreationForm()
    return render(request, 'gestion_libros/registro.html', {'form': form})

# Vista de inicio que redirige a la lista de libros
@login_required
def inicio(request):
    return redirect('lista_libros')

# Vista para listar los libros del usuario autenticado
@login_required
def lista_libros(request):
    libros = Libro.objects.filter(usuario=request.user)
    return render(request, 'gestion_libros/lista_libros.html', {'libros': libros})

# Vista para registrar un nuevo libro
@login_required
def nuevo_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.usuario = request.user  
            libro.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'gestion_libros/nuevo_libro.html', {'form': form})

# Vista para ver los detalles de un libro
@login_required
def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id, usuario=request.user)
    return render(request, 'gestion_libros/detalle_libro.html', {'libro': libro})

# Vista para editar un libro existente
@login_required
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id, usuario=request.user)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('detalle_libro', libro_id=libro.id)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion_libros/editar_libro.html', {'form': form, 'libro': libro})

# Vista para eliminar un libro existente
@login_required
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id, usuario=request.user)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'gestion_libros/eliminar_libro.html', {'libro': libro})
