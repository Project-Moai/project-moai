from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")  # Temporário


def sobre(request):
    return render(request, "sobre.html")  # Temporário


def contato(request):
    return render(request, "contato.html")  # Temporário
