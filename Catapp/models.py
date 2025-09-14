from django.db import models
from django.contrib.auth.models import User

class Dono(models.Model):
    user = models.OneToOneField(User, 
        on_delete=models.CASCADE, 
        related_name='dono_perfil',
        null = True,
        blank=True)

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + " email: " + self.email
    
class Gato(models.Model):
    api_id = models.CharField(
        max_length=100,
        unique= True,
        verbose_name="ID da API")

    raca = models.CharField(max_length=25)
    descricao = models.CharField(max_length=500)

    foto_gato = models.URLField()

    dono = models.ForeignKey(
        Dono, 
        on_delete=models.CASCADE, 
        related_name="dono",
        verbose_name= "dono")

    def __str__(self):
        return self.raca