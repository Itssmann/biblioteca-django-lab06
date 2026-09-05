from django.shortcuts import get_object_or_404, redirect, render

from .forms import AutorForm, LibroForm
from .models import Autor, Libro


def listado_libros(request):
    libros = Libro.objects.select_related("autor").order_by("titulo")
    return render(request, "library/libro_listado.html", {"libros": libros})


def crear_libro(request):
    form = LibroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("library:listado_libros")
    return render(request, "library/libro_formulario.html", {"form": form})


def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=libro)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("library:listado_libros")
    return render(request, "library/libro_formulario.html", {"form": form, "editar": True})


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        libro.delete()
        return redirect("library:listado_libros")
    return render(request, "library/libro_confirmar_eliminar.html", {"libro": libro})


def listado_autores(request):
    autores = Autor.objects.order_by("nombre")
    return render(request, "library/autor_listado.html", {"autores": autores})


def crear_autor(request):
    form = AutorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("library:listado_autores")
    return render(request, "library/autor_formulario.html", {"form": form})


def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("library:listado_autores")
    return render(request, "library/autor_formulario.html", {"form": form, "editar": True})


def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        return redirect("library:listado_autores")
    return render(request, "library/autor_confirmar_eliminar.html", {"autor": autor})
