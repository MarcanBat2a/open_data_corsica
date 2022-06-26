class Commune():
    def __init__(self, name:str, code:str, code_postaux:list[int], code_departement:str, code_region:str, population:int, polygon:list[list[float]]=[]) -> None:
        self.name = name
        self.code = code
        self.code_postaux = code_postaux
        self.code_departement = code_departement
        self.code_region = code_region
        self.population = population
        self.polygon = polygon
        self.list_gares = []
        self.list_bornes_recharges = []
    
    def to_dict(self)->dict:
        return {"name": self.name,
            "code": self.code,
            "code_postaux": self.code_postaux,
            "code_departement": self.code_departement,
            "code_region": self.code_region,
            "population": self.population,
            "polygon": self.polygon,
            "list_gares": [gare.to_dict() for gare in self.list_gares],
            "list_bornes": [borne.to_dict() for borne in self.list_bornes_recharges]
            }