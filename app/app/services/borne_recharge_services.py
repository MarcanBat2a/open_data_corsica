import requests
from app.model.borne_recharge_model import Borne
from app.model.commune_model import Commune

def get_all_borne()->list[Borne]:
    list_bornes = []
    response = requests.get('https://www.data.corsica/api/records/1.0/search/?dataset=fichier-consolide-des-bornes-de-recharge-pour-vehicules-electriques-irve-en-cors&q=&rows=1000&facet=n_enseigne&facet=nbre_pdc&facet=puiss_max&facet=accessibilite&facet=nom_epci&facet=commune&facet=nom_reg&facet=nom_dep')
    for records in response.json().get('records'):
        borne = records.get('fields')
        list_bornes.append(
            Borne(
                borne.get('type_prise'),borne.get('coordonnees'),borne.get('nom_dep'),borne.get('nbre_pdc'),borne.get('n_operateur'),
                borne.get('puiss_max'),borne.get('n_enseigne'),borne.get('nom_epci'),borne.get('code_insee'),borne.get('id_station'),
                borne.get('date_maj'),borne.get('source'),borne.get('commune'),borne.get('reg_code'),borne.get('nom_reg'),borne.get('n_amenageur'),
                borne.get('dep_code'),borne.get('n_station'),borne.get('acces_recharge'),borne.get('ad_station'),borne.get('id_pdc'),
                borne.get('accessibilite'),borne.get('code_epci')
                )
            )

    return list_bornes

