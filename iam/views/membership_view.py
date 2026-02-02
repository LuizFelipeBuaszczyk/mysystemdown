from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from uuid import UUID

from systems.models import System
from iam.services.membership_service import MembershipService
from iam.serializers.membership_serializer import MembershipReadSerializer, MembershipListReadSerializer, MembershipCreateSerializer


@extend_schema_view(
    create=extend_schema(
        request=MembershipCreateSerializer,
        responses={201: MembershipReadSerializer},
        parameters=[
            OpenApiParameter(
                name="system_pk",
                type=UUID,
                location=OpenApiParameter.PATH,
                description="System's UUID"
            )
        ]
    )
)
class MembershipViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]       

    def get(self, request, system_pk=None):
        system = get_object_or_404(System, id=system_pk)
        memberships = MembershipService.get_membership_by_system(system)  
        
        serializer = MembershipListReadSerializer(memberships)
        return Response(serializer.data, status=200)

    def create(self, request, system_pk=None):
        system = get_object_or_404(System, id=system_pk)
        serializer = MembershipCreateSerializer(request.data)
        serializer.is_valid(raise_exception=True)

        membership = MembershipService.create_membership(
            data=serializer.validated_data,
            system=system,
            user=request.user
        )

        serializer = MembershipReadSerializer(membership)
        return Response(serializer.data, status=201)
