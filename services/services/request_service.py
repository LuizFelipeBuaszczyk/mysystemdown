
from services.repositories.request_repository import RequestRepository 
from systems.models import Service

class RequestService:
    
    @staticmethod
    def list_requests_by_service(service: Service):
        return RequestRepository.get_all_by_service(service)