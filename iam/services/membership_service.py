from iam.repositories.membership_repository import MembershipRepository

class MembershipService:
    
    @staticmethod
    def create_membership(data: dict):
        return MembershipRepository.crate_membership(data)