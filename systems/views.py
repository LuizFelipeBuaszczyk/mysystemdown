from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import SystemReadSerializer, SystemWriteSerializer
from .services.system_service import SystemService


# Create your views here.
class SystemViewSet(ViewSet):
    
    def list(self, request):
        systems = SystemService.list_systems()
        serializer = SystemReadSerializer(systems, many=True)
        
        return Response(serializer.data)
    
    def create(self, request):
        serializer = SystemWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        system = SystemService.create_system(serializer.validated_data)
        
        return Response(
            SystemReadSerializer(system).data,
            status=status.HTTP_201_CREATED
        )