from django.urls import include, path

urlpatterns = [
    path("", include("core.urls")),
    path("library/", include("library.urls")),
]
