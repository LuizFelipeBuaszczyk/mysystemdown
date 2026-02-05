from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from uuid import UUID

from iam.permissions.request_permissions import RequestPermission
from systems.models import Service 
from services.services.request_service import RequestService

from services.serializers.request_serializer import RequestListReadSerializer 

class RequestViewSet(GenericViewSet):
    permission_classes = [RequestPermission]
    
    def list(self, request, service_pk=None):
        service = get_object_or_404(Service, id=service_pk)
        
        requests = RequestService.list_requests_by_service(service)
        
        return Response(
            data=RequestListReadSerializer(requests).data, 
            status=status.HTTP_200_OK
            )
        
