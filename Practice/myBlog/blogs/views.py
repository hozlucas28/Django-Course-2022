# Importaciones
from django.shortcuts import render
from .models import Post


# ---------------------------------- Páginas --------------------------------- #

# Inicio.
def index(request):
    firstPost = Post.objects.first()  # Obtengo el primer registro de la base de datos.
    posts = Post.objects.all()
    return render(request, "blogs.html", {"firstPost": firstPost, "posts": posts})


# Posteo
def post(request, id):
    post = Post.objects.get(id=id)  # Obtengo la publicación con la ID enviada.
    print(post.content)
    return render(request, "post.html", {"post": post})
