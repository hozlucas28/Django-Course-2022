from django.http import HttpResponse


# ---------------------------------- Páginas --------------------------------- #

# Página que recibe una variable llamada: 'numbers'
def hello(request):
    numbers = [
        int(n) for n in request.GET["numbers"].split(",")
    ]  # Convierte el String en un Array, y sus elementos en enteros (Int).
    numbers = sorted(numbers)  # Ordena de menor a mayor el Array.
    return HttpResponse(str(numbers))


# Página que verifica la edad enviada a travez de la URL
def verifyAge(request, name, age):
    if age < 12:
        message = f"Hola {name}, no puedes ingresar."
    else:
        message = f"Hola {name}, puedes ingresar."
    return HttpResponse(message)
