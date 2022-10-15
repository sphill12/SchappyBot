import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_details(pokemon: str, description: str | list) -> str | list:
    # request the page containing information on the pokemon
    url = BASE_URL + pokemon.lower()
    response = requests.get(url)
    data = json.loads(response.text)
    if type(description) == list:
        for i in description:
            return data[i]
    else:
        return data[description]

def attribute_list(pokemon: str)-> list:
    url = BASE_URL + pokemon.lower()
    response = requests.get(url)
    data = json.loads(response.text)
    return data.keys()