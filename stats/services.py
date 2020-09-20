import requests


def get_population(place, year=None):
    url = f'http://localhost:8000/api/v1/stats/population/{place}/'
    params = {'year': year}
    # params = {}
    r = requests.get(url, params=params)
    population = r.json()
    population_list = {'population': population['results']}
    return population_list
