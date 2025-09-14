from django.urls import path
from .views import homepage, sobre, DonoCriateView, DonoListView, DonoUpdateView, GatoListView

urlpatterns = [
    path('', homepage, name="homepage"),
    path('Sobre/', sobre, name="sobre"),
    path('User/', DonoCriateView.as_view(), name="criar_usuario"),
    path('Lista/', DonoListView.as_view(), name="lista_donos"),
    path('Lista/', DonoUpdateView.as_view(), name="update_lista"),
    path('listagato/', GatoListView.as_view(), name="listagato"),
]