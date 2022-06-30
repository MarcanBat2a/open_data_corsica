import requests
from app.app.model.care_model import Care
from app.app.model.commune_model import Commune

def get_all_care()->list[Care]:
    list_cares = []
    response = requests.get('https://www.data.corsica/api/records/1.0/search/?dataset=horaires-cars2a-gtfs&q=&rows=1000&facet=stop_name')
    for records in response.json().get('records'):
        care = records.get('fields')
        list_cares.append(Care(care.get("location_type"), care.get("stop_id"), care.get("stop_coordinates"), care.get("stop_code"), care.get("stop_name")))
    return list_cares


def get_all_care_to_dict()->dict[Care]:
    dict_cares = {}
    response = requests.get('https://www.data.corsica/api/records/1.0/search/?dataset=horaires-cars2a-gtfs&q=&rows=1000&facet=stop_name')
    for records in response.json().get('records'):
        care = records.get('fields')
        dict_cares[care.get('stop_id')] = Care(care.get("location_type"), care.get("stop_id"), care.get("stop_coordinates"), care.get("stop_code"), care.get("stop_name")).to_dict()

    return dict_cares


def get_commune_for_all_care()->dict[Care]:
    list_cares = get_all_care()
    dict_cares = {}
    for care in list_cares:
        response = requests.get('https://geo.api.gouv.fr/communes?lat='+str(care.stop_coordinates[0])+'&lon='+str(care.stop_coordinates[1])+'&fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre')
        for records in response.json():
            care.commune = Commune(records.get('nom'), records.get('code'), records.get('codesPostaux'), records.get('codeDepartement'), records.get('codeRegion'), records.get('population'))
            dict_cares[care.get('stop_id')] = care
    return care


def get_commune_by_care(care:Care)->Care:
    
    response = requests.get('https://geo.api.gouv.fr/communes?lat='+str(care.stop_coordinates[0])+'&lon='+str(care.stop_coordinates[1])+'&fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre')
    for records in response.json():
        care.commune = Commune(records.get('nom'), records.get('code'), records.get('codesPostaux'), records.get('codeDepartement'), records.get('codeRegion'), records.get('population'))

    return care