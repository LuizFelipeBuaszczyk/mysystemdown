
from systems.models import System

class SystemRepository:       
    
    @staticmethod
    def get_all():
        return System.objects.values()
    
    @staticmethod
    def get_by_name(name: str):
        return System.objects.filter(name=name).values()
    
    @staticmethod
    def create_system(data: dict):
        return System.objects.create(**data)
    