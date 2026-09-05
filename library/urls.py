from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    path("libros/", views.listado_libros, name="listado_libros"),
    path("libros/nuevo/", views.crear_libro, name="crear_libro"),
    path("libros/<int:pk>/editar/", views.editar_libro, name="editar_libro"),
    path("libros/<int:pk>/eliminar/", views.eliminar_libro, name="eliminar_libro"),
    path("autores/", views.listado_autores, name="listado_autores"),
    path("autores/nuevo/", views.crear_autor, name="crear_autor"),
    path("autores/<int:pk>/editar/", views.editar_autor, name="editar_autor"),
    path("autores/<int:pk>/eliminar/", views.eliminar_autor, name="eliminar_autor"),
]
