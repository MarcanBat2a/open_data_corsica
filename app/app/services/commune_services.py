import requests
from app.services import gare_services, borne_recharge_services
from app.model.commune_model import Commune
from app.model.gare_model import Gare
from app.model.borne_recharge_model import Borne

def get_all_communes()->dict[Commune]:
    dict_communes = {}
    response = requests.get('https://geo.api.gouv.fr/communes?codeRegion=94&fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=contour')
    for records in response.json():
        dict_communes[records.get('code')] = Commune(records.get('nom'), records.get('code'), records.get('codesPostaux'), records.get('codeDepartement'), records.get('codeRegion'), records.get('population')).to_dict()
    
    return dict_communes


def get_gares_for_all_commune(dict_communes:dict[Commune], list_gares:list[Gare])->dict[Commune]:
    for gare in list_gares:
        gare = gare_services.get_commune_by_gare(gare)
        if dict_communes.get(gare.commune.code) != None:
            dict_communes[gare.commune.code]["list_gares"].append(gare.to_dict())
    return dict_communes


def get_bornes_for_all_commune(dict_communes:dict[Commune], list_bornes:list[Borne])->dict[Commune]:
    for borne in list_bornes:
        if dict_communes.get(borne.code_insee) != None:
            dict_communes[borne.code_insee]["list_bornes"].append(borne.to_dict())
    return dict_communes