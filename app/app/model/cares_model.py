class Gare():
    def __init__(self, location_type:str, stop_id:str, stop_coordinates:list[float], stop_code:str, stop_name:str) -> None:
        self.location_type = location_type
        self.stop_id = stop_id
        self.stop_coordinates = stop_coordinates
        self.stop_code = stop_code
        self.stop_name = stop_name
        self.commune = ''

    def to_dict(self)->dict:
        return {
            "location_type": self.location_type,
            "stop_id": self.stop_id,
            "stop_coordinates": self.stop_coordinates,
            "stop_code": self.stop_code,
            "stop_name": self.stop_name,
            "commune": self.commune
            }








