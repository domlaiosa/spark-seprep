import requests

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            return posts['value']
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
    return None

print(get_joke())

