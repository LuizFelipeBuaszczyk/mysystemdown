from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from users.serializers import UserReadSerializer, UserWriteSerializer
from users.services.user_service import UserService

# Create your views here.
class UserViewSet(ViewSet):
    
    def create(self, request):
        serializer = UserWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = UserService.create_user(serializer.validated_data)
        
        return Response(
            UserReadSerializer(user).data,
            status=status.HTTP_201_CREATED
        )