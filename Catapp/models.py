from django.db import models

class Dono(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    endereco = models.CharField(max_length=120)

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