import requests

def informacion_por_nombre(nombre):
    URL = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}/"
    inf = requests.get(URL)

    if inf.status_code == 200:
        datos = inf.json()

        print(datos)

informacion_por_nombre("pikachu")