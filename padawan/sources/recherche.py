import requests
import json

class recherche():
    def __init__(self):
        self.checkRequest = lambda request : json.loads(request.text) if request.status_code == 200 or request.status_code == 201  else {"etat": "error "}
    
    def findDataApi(self, urlAPI):
        try:
            req = requests.get(urlAPI)
            print(req)
            result = self.checkRequest(req)
        except Exception as e:
            result = {"etat": "error "+ str(e)}
        return result
    
    def findFilms(self):
        pass
    
    def findFilms(self, listFilm):
        all_films = []
        for filmUrl in listFilm:
            info_film = self.findDataApi(filmUrl)
            data = {
                "title": info_film['title'],
                "episode_id": info_film['title'],
                "description": info_film['opening_crawl'],
                "producer": info_film['producer'],
                "director": info_film['director'],
                "release_date": info_film['release_date'],
            }
            all_films.append(data)
        return all_films
    
    def findStarships(self, list_starships):
        all_result = []
        for start in list_starships:
            info_start = self.findDataApi(start)
            data = {
                "name": info_start['name'],
                "model": info_start['model'],
                "manufacturer": info_start['manufacturer'],
                "cost_in_credits": info_start['cost_in_credits'],
                "length": info_start['length'],
                "max_atmosphering_speed": info_start['max_atmosphering_speed'],
                "crew": info_start['crew'],
                "passengers": info_start['passengers'],
                "cargo_capacity": info_start['cargo_capacity'],
                "consumables": info_start['consumables'],
                "hyperdrive_rating": info_start['hyperdrive_rating'],
                "MGLT": info_start['MGLT'],
                "starship_class": info_start['starship_class'],
            }
            all_result.append(data)
        return all_result
    
    def findVehicule(self, list_vehicule):
        all_result = []
        for vehicule in list_vehicule:
            info_vehicule = self.findDataApi(vehicule)
            data = {
                "name": info_vehicule['name'],
                "model": info_vehicule['model'],
                "manufacturer": info_vehicule['manufacturer'],
                "cost_in_credits": info_vehicule['cost_in_credits'],
                "length": info_vehicule['length'],
                "max_atmosphering_speed": info_vehicule['max_atmosphering_speed'],
                "crew": info_vehicule['crew'],
                "passengers": info_vehicule['passengers'],
                "cargo_capacity": info_vehicule['cargo_capacity'],
                "consumables": info_vehicule['consumables'],
                "vehicle_class": info_vehicule['vehicle_class'],
            }
            all_result.append(data)
        return all_result
    
    def peopleList(self):
        urlAPI = "https://swapi.dev/api/people"
        dataList = self.findDataApi(urlAPI)
        result = []
        for people in dataList['results']:
            data = {
                "name": people['name'],
                "gender": people['gender'],
                "height": people['height'],
                "hair_color": people['hair_color'],
                "height": people['height'],
                "skin_color": people['skin_color'],
                "birth_year": people['birth_year'],
                "films": self.findFilms(people['films']),
                # "starships": self.findStarships(people['starships']),
                # "vehicles": self.findVehicule(people['vehicles']),
            }
            result.append(data)
        data['next'] = dataList['next']
        return  result
    
    def filterFunction(self, tabKey):
        pass

        