from django.urls import path
from .views import homepage, sobre, adotar_gato, login_view, DonoCriateView, DonoListView, DonoUpdateView,DonoDeleteView, GatoListView

urlpatterns = [
    path('', homepage, name="homepage"),
    path('Sobre/', sobre, name="sobre"),
    path('login/', login_view, name="login"),


    path('User/', DonoCriateView.as_view(), name="criar_usuario"),
    path('Lista/', DonoListView.as_view(), name="lista_donos"),
    path('Lista/<int:pk>/update', DonoUpdateView.as_view(), name="update_lista"),
    path('delete/<int:pk>', DonoDeleteView.as_view(), name="deletar_user"),


    path('listagato/', GatoListView.as_view(), name="listagato"),
    path('adotar/<int:gato_id>', adotar_gato, name="adotar_gato"),
]