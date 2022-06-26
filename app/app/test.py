from services import gare_services, commune_services, borne_recharge_services
import json

#for gare in gare_services.get_all_gare():
#    print(gare_services.get_commune_by_gare(gare).to_dict())
list_gares = gare_services.get_all_gare()
list_bornes = borne_recharge_services.get_all_borne()
dict_commmune = commune_services.get_all_communes()
dict_commmune = commune_services.get_gares_for_all_commune(dict_commmune, list_gares)
dict_commmune = commune_services.get_bornes_for_all_commune(dict_commmune, list_bornes)
#print(commune_services.get_gares_for_all_commune(dict_commmune, list_gares))

import pandas as pd

with open('data.json', 'w') as json_file:
  json.dump(dict_commmune, json_file)

df = pd.DataFrame(data=dict_commmune.values())

df = (df.T)

print (df)

df.to_excel('dict1.xlsx')