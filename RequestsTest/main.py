import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '536fd3f6ed7c56bd850643cba73bc647'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}
body_name = {
    "pokemon_id": "328184",
    "name": "Бульба",
    "photo_id": 12
}
body_pokeball = {
    "pokemon_id": "328184"
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)'''