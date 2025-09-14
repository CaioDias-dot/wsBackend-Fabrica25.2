from django import forms
from .models import Dono,Gato

class DonoForm(forms.ModelForm):
    class Meta:
        model = Dono
        fields = ['nome', 'email', 'senha']

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)

class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = ['api_id','raca','descricao','foto_gato','dono']