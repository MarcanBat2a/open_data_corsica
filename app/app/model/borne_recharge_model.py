class Borne():
    def __init__(self, type_prise: str, coordonnees: list[float], nom_dep:str, nbre_pdc:int, n_operateur:str, 
    puiss_max:float, n_enseigne:str, nom_epci:str, code_insee:str, id_station:str, date_maj:str, source:str, commune:str, reg_code:str, 
    nom_reg:str, n_amenageur:str, dep_code:str, n_station:str, acces_recharge:str, ad_station:str, id_pdc:str, accessibilite:str, code_epci:str) -> None:
        self.type_prise = type_prise
        self.coordonnees = coordonnees
        self.nom_departement = nom_dep
        self.nombre_point_de_charge = nbre_pdc
        self.operateur = n_operateur
        self.puissance_max = puiss_max
        self.enseigne = n_enseigne
        self.nom_epci = nom_epci
        self.code_insee = code_insee
        self.id_station = id_station
        self.date_maj = date_maj
        self.source = source
        self.commune = commune
        self.reg_code = reg_code
        self.nom_reg = nom_reg
        self.amenageur = n_amenageur
        self.dep_code = dep_code
        self.nom_station = n_station
        self.condition_accès = acces_recharge
        self.adresse_station = ad_station
        self.id_point_de_charge = id_pdc
        self.accessibilite = accessibilite
        self.code_epci = code_epci

    def to_dict(self)->dict:
        return {
            'type_prise': self.type_prise,
            'coordonnees': self.coordonnees,
            'nom_departement': self.nom_departement,
            'nombre_point_de_charge': self.nombre_point_de_charge,
            'operateur': self.operateur,
            'puissance_max': self.puissance_max,
            'enseigne': self.enseigne,
            'nom_epci': self.nom_epci,
            'code_insee': self.code_insee,
            'id_station': self.id_station,
            'date_maj': self.date_maj,
            'source': self.source,
            'commune': self.commune,
            'reg_code': self.reg_code,
            'nom_reg': self.nom_reg,
            'amenageur': self.amenageur,
            'dep_code': self.dep_code,
            'nom_station': self.nom_station,
            'condition_accès': self.condition_accès,
            'adresse_station': self.adresse_station,
            'id_point_de_charge': self.id_point_de_charge,
            'accessibilite': self.accessibilite,
            'code_epci': self.code_epci
            }