from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
class User(AbstractUser):
    username = None
    
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email" # Informa que o Campo de login é o email
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email