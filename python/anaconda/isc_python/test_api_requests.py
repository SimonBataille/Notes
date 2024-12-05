'''
api permet a un logiciel de demander une action a un autre logiciel
https://geo.api.gouv.fr/decoupage-administratif/communes#postal-code
curl 'https://geo.api.gouv.fr/communes?codePostal=78000'
'''

import requests

url = 'https://geo.api.gouv.fr/communes'

params = {
    'codePostal': '78000'
}

response = requests.get(url, params=params)

print(response) 

if response.status_code == 200:
    print (response.json())
