from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("servicos/", views.servicos, name="servicos"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("contato/", views.contato, name="contato"),
    path("faq/", views.faq, name="faq"),
]
