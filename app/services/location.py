import googlemaps
import requests, json, time
from bs4 import BeautifulSoup


GOOGLE_API_KEY = 'AIzaSyDhb8JEjwwnqsCiBOm_hHVOlxNfXbGOy14'
gmaps = googlemaps.Client(GOOGLE_API_KEY)

def scrape_site():
    r       = requests.get('https://schedules.wsu.edu/Home/Buildings', requests.utils.default_headers())
    soup    = BeautifulSoup(r.content, 'html.parser')
    table   = soup.find('table', {'id': 'buildings'})
    
    halls = []
    for row in table.findAll('tr'):
        aux = row.findAll('td')
        if aux[2].string and aux[2].string == 'Pullman Campus':
            halls.append({
                'name': aux[1].string.strip(),
                'abbr': aux[0].string.strip().upper(),
                'x': 0,
                'y': 0
            })

    return halls


def hall_to_coordinates(query):
    gmaps.places(query)['results'][0]

    results = gmaps.places('{}, Pullman, WA'.format(query))['results']
    if results == []:
        return 0,0

    results = results[0]['geometry']['location']

    return results['lng'], results['lat']


def to_json():
    halls = scrape_site()
    for hall in halls:
        hall['x'], hall['y'] = hall_to_coordinates(hall['name'])
    
    json_out            = {}
    json_out['written'] = int(time.time())
    json_out['halls']   = halls

    with open('static/data/wsu_halls.json', 'r+') as f:
        json.dump(json_out, f)

    return json_out


def get_halls():
    with open('static/data/wsu_halls.json', 'r+') as f:
        data = json.load(f)

    if data['written'] and data['written'] + 2592000 < time.time(): # 30 days in seconds 
        return to_json()
    else:
        return data

def get_distance(hall, current): # hall object, then current location tuple
    x = float(hall.x) - float(current[0])
    y = float(hall.y) - float(current[1])
    return (x**2 + y**2)**.5