from systems.repositories.system_repository import SystemRepository

class SystemService:
    
    @staticmethod
    def list_systems():
        return SystemRepository.get_all()        
    
    @staticmethod
    def create_system(data: dict):        
        return SystemRepository.create_system(data)