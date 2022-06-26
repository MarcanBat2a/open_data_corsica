from abc import ABC


class BaseManager(ABC):
    def __init__(self, adapter) -> None:
        self.adapter = adapter


    def get_all(self):
        list_object = []
        for adapter in self.adapter.get_all():
            list_object.append(adapter.to_dict())    
        return list_object
