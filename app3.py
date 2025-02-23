import requests
import json
from pathlib import Path

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
            })
else:
    print(f"O erro foi {response.status_code}")

print(dados_restaurante)
caminho_pasta = Path("./restaurantes")
caminho_pasta.mkdir(parents=True, exist_ok=True)
for nome_restaurante, dados in dados_restaurante.items():
    caminho_arquivo = caminho_pasta / f'{nome_restaurante}.json'
    with open(caminho_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)