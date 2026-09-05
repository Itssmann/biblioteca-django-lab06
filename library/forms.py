from django import forms

from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "nacionalidad"]


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "isbn", "anio", "disponible"]
