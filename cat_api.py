# Código feito para popular os gatos no banco de dados

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wsCatFinder.settings")
django.setup()

import requests
from Catapp.models import Gato, Dono

#Essa função deixa todos os gatos por padrão "sem dono".
dono_inexistente, _ = Dono.objects.get_or_create(
    email="none@gmail.com",
    defaults={
        "nome": "Sem Dono",
        "endereco": "none",
    }
)

url = "https://api.thecatapi.com/v1/breeds"
headers = {"x-api-key": "live_FwoUVTgFCyt4S7wecLoIiwqpGxfFCTNGXndNylGCwSKKprQ06Ve1UtFVFsavZyOp"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    dados_gato = response.json()

    for breed in dados_gato:
        api_id      = breed.get("id")
        raca        = breed.get("name", "Sem raça")
        descricao   = breed.get("description", "Sem descrição")
        foto   = breed.get("image", {}).get("url", "https://placekitten.com/400/400")

        Gato.objects.create(
            api_id      = api_id,
            raca        = raca,
            descricao   = descricao,
            foto_gato   = foto,
            dono        = dono_inexistente,
        )