from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "./home/pages/index.html")


def sobre(request):
    return render(request, "./home/pages/about.html")


def contato(request):
    return render(request, "./home/pages/contact.html")


def servicos(request):
    return render(request, "./home/pages/services.html")


def portfolio(request):
    return render(request, "./home/pages/portfolio.html")


def faq(request):
    return render(request, "./home/pages/faq.html")
