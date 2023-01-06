# ------------------------------------------------------------------------- #
# APUNTES:
# 		   XXX.
#
#
# IMPORTANTE:
#  			  - <MODELO>.objects.all() = Devuelve todos los registros.
#  			  - <MODELO>.get(id=<ID>) = Devuelve el registro de dicha id.
#  			  - <MODELO>.get(id=<ID>).delete() = Elimina el registro de dicha id.
# ------------------------------------------------------------------------- #

# Importaciones
from django.shortcuts import render
from .models import Project


# ---------------------------------- Vistas ---------------------------------- #

# Inicio.
def index(request):
    projects = Project.objects.all()
    return render(request, "profile.html", {"projects": projects})
