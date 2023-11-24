from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "Home",
        "description": "Página inicial",
    }
    return render(request, "./home/pages/index.html", context)


def sobre(request):
    context = {
        "title": "Sobre",
        "description": "Página sobre",
    }
    return render(request, "./home/pages/about.html", context)


def contato(request):
    context = {
        "title": "Contato",
        "description": "Página de contato",
    }
    return render(request, "./home/pages/contact.html", context)


def servicos(request):
    context = {
        "title": "Serviços",
        "description": "Página de serviços",
    }
    return render(request, "./home/pages/services.html", context)


def portfolio(request):
    context = {
        "title": "Portfolio",
        "description": "Página de portfolio",
    }
    return render(request, "./home/pages/portfolio.html", context)


def faq(request):
    context = {
        "title": "FAQ",
        "description": "Página de FAQ",
    }
    return render(request, "./home/pages/faq.html", context)


def ajuda(request):
    context = {
        "title": "Ajuda",
        "description": "Página de ajuda",
    }
    return render(request, "./home/pages/help.html", context)


def privacidade(request):
    context = {
        "title": "Privacidade",
        "description": "Página de privacidade",
    }
    return render(request, "./home/pages/privacy.html", context)


def acessibilidade(request):
    context = {
        "title": "Acessibilidade",
        "description": "Página de acessibilidade",
    }
    return render(request, "./home/pages/accessibility.html", context)


def redes_sociais(request):
    context = {
        "title": "Redes Sociais",
        "description": "Página de Redes Sociais",
    }
    return render(request, "./home/pages/social-media.html", context)


def aplicativo(request):
    context = {
        "title": "Aplicativo",
        "description": "Página de Aplicativo",
    }
    return render(request, "./home/pages/app.html", context)


def termos(request):
    context = {
        "title": "Termos",
        "description": "Página de Termos",
    }
    return render(request, "./home/pages/terms.html", context)
