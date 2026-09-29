from django import forms

from .models import Autor, Categoria, Editorial, FichaAutor, Lector, Libro, Prestamo


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "nacionalidad"]


class FichaAutorForm(forms.ModelForm):
    class Meta:
        model = FichaAutor
        fields = ["biografia", "foto_url", "sitio_web"]


class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ["nombre", "pais"]


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]


class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ["nombre", "email", "telefono"]


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "editorial", "categoria", "isbn", "anio", "disponible"]


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ["libro", "lector", "fecha_devolucion_esperada", "devuelto"]
