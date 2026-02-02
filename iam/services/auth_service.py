from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from iam.exceptions import InvalidCredentialsError, UserInactiveError, AccountNotVerifiedError

class AuthService:
    
    @staticmethod
    def login(data: dict):
        email = data.get("email")
        password = data.get("password")
        
        user = authenticate(email=email, password=password)
        if not user:
            raise InvalidCredentialsError("Invalid email or password")
        if not user.is_active:
            raise UserInactiveError("User is inactive")
        if not user.is_verified:
            raise AccountNotVerifiedError("User is not verified")
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        
        return {
            "access_token": access_token,
            "refresh": str(refresh)
        }