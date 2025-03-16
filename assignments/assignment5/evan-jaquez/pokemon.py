import requests
import random

def get_random_pokemon():
    # Generate a random Pokémon ID (1 to 1010 as of now)
    pokemon_id = random.randint(1, 1010)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            pokemon_name = result['name']
            print(f"Random Pokémon: {pokemon_name.capitalize()}")
        else:
            print(f"Error: Unable to get data, status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Call the function
get_random_pokemon()
