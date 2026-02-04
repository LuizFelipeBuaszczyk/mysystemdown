from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from uuid import UUID

from systems.services.bot_service import BotService
from systems.models import System, Bot
from systems.serializers.bot_serializer import BotReadSerializer, BotWriteSerializer

@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name="system_pk",
                type=UUID,
                location=OpenApiParameter.PATH,
                description="System's UUID"
            ),
        ]
    ),
    create=extend_schema(
        request=BotWriteSerializer,
        responses={201: BotReadSerializer},
        parameters=[
            OpenApiParameter(
                name="system_pk",
                type=UUID,
                location=OpenApiParameter.PATH,
                description="System's UUID"
            ),
        ]
    )
)
class BotViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Bot.objects.none()
    
    def get_serializer_class(self):
        if self.action == "create":
            return BotWriteSerializer
        return BotReadSerializer
    
    def list(self, request, system_pk: UUID):
        system = get_object_or_404(System.objects.filter(membership__user=request.user), id=system_pk)
        bots = BotService.get_all(system=system)
        
        return Response(
            data=BotReadSerializer(bots, many=True).data,
            status=status.HTTP_200_OK
        )
    
    def create(self, request, system_pk: UUID):
        system = get_object_or_404(System.objects.filter(membership__user=request.user), id=system_pk)

        serializer = BotWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        bot = BotService.create_bot(
            data=serializer.validated_data,
            system=system
        )
        
        return Response(
            BotReadSerializer(bot).data,
            status=status.HTTP_201_CREATED
        )