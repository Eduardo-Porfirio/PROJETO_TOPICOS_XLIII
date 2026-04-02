from django.shortcuts import render
from django.http import HttpResponse

def pagina_produtos(request):
    return HttpResponse("Página de produtos!")

def pagina_celulares(request):
    return HttpResponse("Página de celulares!")