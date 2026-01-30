from users.repositories.user_repository import UserRepository
from users.models import User

class UserService:
    
    @staticmethod
    def create_user(data: dict):
        return UserRepository.create_user(data)
    
    @staticmethod
    def get_user_by_email(email: str):
        return UserRepository.get_user_by_email(email)