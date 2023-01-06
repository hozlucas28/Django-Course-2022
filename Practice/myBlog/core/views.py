# Importación
from django.shortcuts import render


# ---------------------------------- Páginas --------------------------------- #

# Inicio
def index(request):
    return render(request, "index.html")
