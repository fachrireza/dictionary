import requests

api_key = 'bb7399a1-b021-43ed-889f-41cb24080077'
word = 'tomato'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)