class Gare():
    def __init__(self, stop_id:str, stop_code:str, stop_coordinates:list[float], stop_name:str) -> None:
        self.stop_id = stop_id
        self.stop_code = stop_code
        self.name = stop_name
        self.location = stop_coordinates
        self.commune = ''

    def to_dict(self)->dict:
        return {
            "stop_id": self.stop_id,
            "name": self.name,
            "stop_code": self.stop_code,
            "location": self.location,
            "commune": self.commune
            }