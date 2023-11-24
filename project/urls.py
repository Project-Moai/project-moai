"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", include("home.urls"), name="index"),
    path("faq/", include("home.urls"), name="faq"),
    path("ajuda/", include("home.urls"), name="ajuda"),
    path("sobre/", include("home.urls"), name="sobre"),
    path("termos/", include("home.urls"), name="termos"),
    path("contato/", include("home.urls"), name="contato"),
    path("servicos/", include("home.urls"), name="servicos"),
    path("portfolio/", include("home.urls"), name="portfolio"),
    path("aplicativo/", include("home.urls"), name="aplicativo"),
    path("privacidade/", include("home.urls"), name="privacidade"),
    path("redes-sociais/", include("home.urls"), name="redes-sociais"),
    path("acessibilidade/", include("home.urls"), name="acessibilidade"),
]
