from django import forms
from .models import Dono

class DonoForm(forms.ModelForm):
    class Meta:
        model = Dono
        fields = ['nome', 'email', 'endereco']