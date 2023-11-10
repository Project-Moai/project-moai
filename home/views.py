from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "./pages/index.html")


def sobre(request):
    return render(request, "./pages/about.html")


def contato(request):
    return render(request, "./pages/contact.html")
