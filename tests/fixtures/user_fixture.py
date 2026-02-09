import pytest

@pytest.fixture
def user_post_data():
    """Payload base para o endpoint de criação de usuário"""
    return {
        "email": "nM2Y8@example.com",
        "password": "password",
        "first_name": "John",
        "last_name": "Doe"
    }