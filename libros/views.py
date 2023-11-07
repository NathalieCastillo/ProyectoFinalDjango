from django.shortcuts import render, redirect
from.models import Libro
from django.contrib import messages


# Create your views here.

def home(request):
    libroslistados = Libro.objects.all()
    messages.success(request, 'Libros listados!')
    return render(request, "gestion_libros.html", {"libros":libroslistados}) 

def registrarLibro(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    autor = request.POST['txtAutor']

    libro = Libro.objects.create(codigo=codigo, nombre=nombre, autor=autor), 
    messages.success(request, 'Libro registrado!')
    
    return redirect('/')

def edicionLibro(request, codigo):
    libro= Libro.objects.get(codigo=codigo)
    return render(request, "edicion_Libro.html", {"libro":libro})

def editarLibro(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    autor = request.POST['txtAutor']

    libro = Libro.objects.get(codigo=codigo)
    libro.nombre = nombre
    libro.autor = autor 
    libro.save()
    
    messages.success(request, 'Libro actualizado!')

    return redirect('/')

def eliminarLibro(request, codigo):
    libro = Libro.objects.get(codigo=codigo)
    libro.delete()
    
    messages.success(request, 'Libro eliminado!')

    return redirect('/')
