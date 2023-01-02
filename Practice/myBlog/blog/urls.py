# Importaciones
from django.urls import path
from . import views


# Rutas: .../core/<PATRÓN DE URL>
urlpatterns = [
    path("", views.index, name="blog"),  # http://127.0.0.1:8000/blog
    path("<int:id>", views.post, name="post"),  # http://127.0.0.1:8000/blog/4
]
