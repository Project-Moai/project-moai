from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("faq/", views.faq, name="faq"),
    path("ajuda/", views.ajuda, name="ajuda"),
    path("sobre/", views.sobre, name="sobre"),
    path("termos/", views.termos, name="termos"),
    path("contato/", views.contato, name="contato"),
    path("servicos/", views.servicos, name="servicos"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("aplicativo/", views.aplicativo, name="aplicativo"),
    path("privacidade/", views.privacidade, name="privacidade"),
    path("redes-sociais/", views.redes_sociais, name="redes-sociais"),
]
