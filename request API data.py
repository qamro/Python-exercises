import requests

api_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{api_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()  # that will convert our json response to a python dictionary
        print(pokemon_data)
    else:
        print(f"Failed to fetch data {response.status_code}") 
        


# example of pokemon name to perform our function
pokemon_name = "pikachu"
get_pokemon_info(pokemon_name)


"""
NOTE: these are HTTP response status codes
(100 - 199): informational responses
(200 - 299): successful responses
(300 - 399): redirection messages
(400 - 499): client error responses
(500 - 599): server error responses

NOTE: these are some familiar error response:
404: NotFound
403: Forbidden
402: Payment required
401: Unauthorized
400: bad request
"""