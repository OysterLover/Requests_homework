import requests
from pprint import pprint

URL = 'https://www.superheroapi.com/api.php/2619421814940190/search/'
superheroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
intelligence = []
names = []
for heroes in superheroes:
    response = requests.get(URL + heroes['name'])
    (intelligence.append(int(response.json()['results'][0]['powerstats']['intelligence'])))
    names.append(heroes['name'])

# pprint(intelligence)
# pprint(names)

heroes_intelligence_reverted = {intelligence[0]: names[0], intelligence[1]: names[1], intelligence[2]: names[2]}
# print(heroes_intelligence_reverted)
# print(sorted(intelligence))

def the_cleverest():
    print(heroes_intelligence_reverted[sorted(intelligence)[-1]])

the_cleverest()

