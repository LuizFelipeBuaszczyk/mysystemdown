from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

from iam.utils.viewaction_map import get_perm

class MembershipPermission(BasePermission):
    
    def has_permission(self, request, view):
        codename = get_perm(view.action)
        return Group.objects.filter(
            memberships__user=request.user,
            memberships__tenant=request.tenant,
            permissions__codename=f"{codename}_membership"
        ).exists()
    
    def has_object_permission(self, request, view, obj):
        return False