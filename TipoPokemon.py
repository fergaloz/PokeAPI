import requests

def tipo_pokemon(tipo):
    URL = f"https://pokeapi.co/api/v2/type/{tipo.lower()}"
    tipo = requests.get(URL)

    if tipo.status_code == 200:
         datos = tipo.json()
         lista_tipos_de_pokemon = datos["pokemon"]


    print(lista_tipos_de_pokemon)

tipo_pokemon("grass")








