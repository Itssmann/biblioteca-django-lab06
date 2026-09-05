# Biblioteca Django

Proyecto de laboratorio con las aplicaciones `core` y `library`.

## Ejecutar

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py manage.py runserver
```

Visita `http://127.0.0.1:8000/library/` para ver el catálogo.

## Datos en memoria

La aplicación no usa base de datos, modelos de Django, migraciones ni el administrador. Los libros iniciales y los que se agregan se guardan solamente en una lista de diccionarios en `library/models.py`.

Por ese motivo, los libros agregados se pierden cuando se reinicia el servidor; es el comportamiento esperado.
