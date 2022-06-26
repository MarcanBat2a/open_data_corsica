import requests
from app.model.gare_model import Gare
from app.model.commune_model import Commune

def get_all_gare()->list[Gare]:
    list_gares = []
    response = requests.get('https://www.data.corsica/api/records/1.0/search/?dataset=horaires-cfc-gtfs&q=&rows=1000')
    for records in response.json().get('records'):
        gare = records.get('fields')
        list_gares.append(Gare(gare.get('stop_id'), gare.get('stop_code'), gare.get('stop_coordinates'), gare.get('stop_name')))

    return list_gares


def get_all_gare_to_dict()->dict[Gare]:
    dict_gares = {}
    response = requests.get('https://www.data.corsica/api/records/1.0/search/?dataset=horaires-cfc-gtfs&q=&rows=1000')
    for records in response.json().get('records'):
        gare = records.get('fields')
        dict_gares[gare.get('stop_id')] = Gare(gare.get('stop_id'), gare.get('stop_code'), gare.get('stop_coordinates'), gare.get('stop_name')).to_dict()

    return dict_gares


def get_commune_by_gare(gare:Gare)->Gare:
    response = requests.get('https://geo.api.gouv.fr/communes?lat='+str(gare.location[0])+'&lon='+str(gare.location[1])+'&fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre')
    for records in response.json():
        gare.commune = Commune(records.get('nom'), records.get('code'), records.get('codesPostaux'), records.get('codeDepartement'), records.get('codeRegion'), records.get('population'))

    return gare