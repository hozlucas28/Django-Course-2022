# Importaciones
from django.urls import path
from . import views


# Rutas
urlpatterns = [
    path("", views.index, name="blogs"),  # http://127.0.0.1:8000/blogs
    path("<int:id>", views.post, name="post"),  # http://127.0.0.1:8000/blogs/4
]
