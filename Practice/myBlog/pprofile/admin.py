# Importaciones
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "dateCreated",
        "dateUpdated",
    )  # Títulos de las celdas.

    list_editable = ("title",)  # Celdas editables.
    readonly_fields = ("dateCreated", "dateUpdated")
    list_display_links = ("id",)  # Links disponibles al proyecto.

    search_fields = ("title", "description")  # Búsquedas disponibles.
    list_filter = ("title", "dateCreated", "dateUpdated")  # Filtros disponibles.
