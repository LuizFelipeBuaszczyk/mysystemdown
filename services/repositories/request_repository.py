from services.models import Request
from systems.models import Service  

class RequestRepository:
    
    @staticmethod
    def get_all_by_service(service: Service):
        return Request.objects.filter(service=service)