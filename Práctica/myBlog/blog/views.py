# Importaciones
from django.shortcuts import render, HttpResponse
from .models import Post


# ---------------------------------- Páginas --------------------------------- #

# Inicio.
def index(request):
    posts = Post.objects.all()
    return HttpResponse(posts)


# Posteo
def post(request, id):
    post = Post.objects.get(id=id)
    content = f"{post.title} - {post.description}"
    return HttpResponse(content)
