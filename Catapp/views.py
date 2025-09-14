from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate

from .models import Dono, Gato
from .forms import DonoForm,LoginForm, GatoForm

def homepage(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

class DonoCriateView(CreateView):
    model = Dono
    form_class = DonoForm
    template_name = "criar_user.html"
    success_url = reverse_lazy("listagato")

    def form_valid(self, form):
        response = super().form_valid(form)

        dono = self.object
        if dono.user is None:
            senha = form.cleaned_data['senha']
            user = User.objects.create_user(
                username=dono.email,
                email=dono.email,
                password=senha
            )
            dono.user = user
            dono.save()

        return response

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            try:
                user_obj = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'Email inválido.')
                return render(request, 'login.html', {'form': form})

            # autentica usando username e senha, pois django não estava aceitando apenas email e nome
            user = authenticate(request, username=user_obj.username, password=senha)
            if user is not None:
                login(request, user)
                return redirect('listagato')
            else:
                messages.error(request, 'Senha incorreta.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


class DonoListView(ListView):
    model = Dono
    template_name = "lista_donos.html"
    context_object_name = "donos"

class DonoUpdateView(UpdateView):
    model = Dono
    form_class = DonoForm
    template_name = "criar_user.html"
    context_object_name = "donos"
    success_url = reverse_lazy("lista_donos")

class DonoDeleteView(DeleteView):
    model = Dono
    form_class = DonoForm
    template_name = "deletar_user.html"
    context_object_name = "dono"
    success_url = reverse_lazy("lista_donos")

class GatoListView(ListView):
    model = Gato
    form_class = GatoForm
    template_name = "lista_gato.html"
    context_object_name = "gatos"

def adotar_gato(request, gato_id):
    if request.method=='POST':
        gato = get_object_or_404(Gato, id=gato_id)

        try:
            dono = request.User.dono_perfil
        except Dono.DoesNotExist:
            return redirect('criar_usuario')
    
        gato.dono = request.User.dono_perfil
        gato.save()

        return redirect('listagato')
    return redirect('listagato')