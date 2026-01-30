
from iam.models import Membership

class MembershipRepository:
    
    @staticmethod
    def crate_membership(data: dict):
        return Membership.objects.create(**data)