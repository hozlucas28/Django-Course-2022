# Importación
from django.shortcuts import render, HttpResponse


# ---------------------------------- Páginas --------------------------------- #

# Inicio
def index(request):
    return HttpResponse("<h1>Página de Inicio - Core</h1>")
