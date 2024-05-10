from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludo(request):
    return HttpResponse("<h1><p style='color: purple;'>Bienvenidos Todos</p></h1>")
def saludoRojo(request):
    return HttpResponse("<h1><p style='color: red;'>Bienvenidos Todos</p></h1>")
def saludoVerde(request):
    return HttpResponse("<h1><p style='color: green;'>¡Bienvenidos todos!</p></h1>")