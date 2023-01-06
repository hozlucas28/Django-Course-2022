# Importaciones
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "title",
        "description",
        "dateCreated",
        "dateUpdated",
    )  # Títulos de las celdas.

    readonly_fields = ("dateCreated", "dateUpdated")
    list_display_links = ("id", "title")  # Links disponibles al proyecto.

    search_fields = ("title", "description")  # Búsquedas disponibles.
    list_filter = ("dateCreated", "dateUpdated")  # Filtros disponibles.
