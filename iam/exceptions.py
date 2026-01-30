from config.exceptions import AuthenticationError

class InvalidCredentialsError(AuthenticationError):
    default_message = "Invalid credentials"
    default_code = "invalid_credentials"

class UserInactiveError(AuthenticationError):
    default_message = "User account is inactive"
    default_code = "user_inactive"
    
class AccountNotVerifiedError(AuthenticationError):
    default_message = "Account not verified"
    default_code = "account_not_verified"