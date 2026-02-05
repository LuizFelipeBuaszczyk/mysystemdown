from rest_framework.permissions import BasePermission

from systems.models import Service   

class RequestPermission(BasePermission):
    
    def has_permission(self, request, view):
        service_pk = view.kwargs.get("service_pk", None)
        #print(request.headers) # TODO: Implementar validação header -> Token BOT apenas eles poderão inserir
        
        if view.action == "list":
            return Service.objects.filter(
                id=service_pk,
                system__memberships__user=request.user,
                system__memberships__group__permissions__codename="view_request"
            ).exists()
            
        return False
    
    def has_object_permission(self, request, view, obj):
        return True