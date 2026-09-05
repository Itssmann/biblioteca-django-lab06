from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    nacionalidad = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
    isbn = models.CharField(max_length=20)
    anio = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
