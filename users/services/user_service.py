from users.repositories.user_repository import UserRepository
from users.models import User

class UserService:
    
    @staticmethod
    def create_user(data: dict):
        #TODO: Após implementar a verificação do email, remover essa linha
        data['is_verified'] = True
        return UserRepository.create_user(data)
    
    @staticmethod
    def get_user_by_email(email: str):
        return UserRepository.get_user_by_email(email)