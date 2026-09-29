from django.contrib import admin

from .models import Autor, Categoria, Editorial, FichaAutor, Lector, Libro, Prestamo


# ---------- Inlines ----------

class FichaAutorInline(admin.StackedInline):
    """Expone la relación OneToOneField (Autor - FichaAutor) dentro de
    la propia pantalla del Autor. StackedInline porque es un único
    registro relacionado (1:1), con formulario apilado en vertical."""
    model = FichaAutor
    can_delete = True
    extra = 0
    verbose_name_plural = "Ficha biográfica"


class PrestamoInline(admin.TabularInline):
    """Expone el modelo intermedio (through) de la relación ManyToManyField
    (Libro <-> Lector, a través de Prestamo) dentro de la pantalla del
    Libro. TabularInline porque pueden existir varios préstamos por libro,
    mostrados como filas de una tabla editable."""
    model = Prestamo
    extra = 1
    fields = ("lector", "fecha_devolucion_esperada", "devuelto")
    readonly_fields = ()


# ---------- ModelAdmin personalizados ----------

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nacionalidad", "tiene_ficha")
    search_fields = ("nombre", "nacionalidad")
    inlines = [FichaAutorInline]

    @admin.display(description="Tiene ficha", boolean=True)
    def tiene_ficha(self, obj):
        return hasattr(obj, "ficha")


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "editorial", "categoria", "anio", "disponible")
    list_filter = ("disponible", "categoria", "editorial")
    search_fields = ("titulo", "isbn", "autor__nombre")
    inlines = [PrestamoInline]


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais")
    search_fields = ("nombre",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")


@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "telefono")
    search_fields = ("nombre", "email")


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("libro", "lector", "fecha_prestamo", "fecha_devolucion_esperada", "devuelto")
    list_filter = ("devuelto", "fecha_devolucion_esperada")
    search_fields = ("libro__titulo", "lector__nombre")


# FichaAutor no se registra de forma independiente en el panel principal
# porque ya se edita a través del Inline de Autor (Ejercicio 6/11).
# Se registra igualmente para cumplir el Ejercicio 3/9 (registrar las 7
# entidades) y permitir verla también de forma directa si se necesita.
admin.site.register(FichaAutor)
