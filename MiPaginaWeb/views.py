from datetime import datetime
from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("hola")

def segunda_vista(request):
    return HttpResponse("Chau pa")

def diaHoy(request):
    dia = datetime.datetime.now()

    texto = f"Hoy dia es {dia}"

    return HttpResponse(texto)