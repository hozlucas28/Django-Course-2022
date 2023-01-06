# Importaciones
from django.urls import path
from . import views

# Rutas
urlpatterns = [path("", views.index, name="home")]  # http://127.0.0.1:8000/
