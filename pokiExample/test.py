import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

data = json.loads(response.text)
print(data)



for ability in data["abilities"]:
  print(ability["ability"]["name"])