# Importaciones
from django.urls import path
from . import views


# Rutas: .../profile/<PATRÓN DE URL>
urlpatterns = [path("", views.index, name="profile")]  # http://127.0.0.1:8000/profile/
