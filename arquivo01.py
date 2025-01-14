import requests


def pegar_pokemon(id: int) -> PokemonSchame:

    URL = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(URL)

    data = response.json()
    data_types = data['types']
    type_list = []
    for type_info in data_types:
        type_list.append(type_info['type']['name'])

    types = ', '.join(type_list)

    return PokemonSchame(name=data['name'], type=types)

if __name__ == "__main__":
    print(pegar_pokemon(50))
    print(pegar_pokemon(34))
    print(pegar_pokemon(27))