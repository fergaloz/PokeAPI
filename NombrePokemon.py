import requests

def nombre_pokemon(nombre):
    URL = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    nombre = requests.get(URL)

    if nombre.status_code == 200:
        datos = nombre.json()
        datos_nombre = datos["name"]

        print(f"¡Es {datos_nombre}!")

nombre_pokemon("charmander")
