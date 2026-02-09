import pytest
from tenants.models import Client, Domain
from rest_framework.test import APIClient
from django.core.management import call_command
from django_tenants.utils import schema_context

@pytest.fixture(scope="session")
def tenant(django_db_setup, django_db_blocker):
    """Inicializa setup inicial para os testes.
    ---
    - django_db_setup: Garante que o banco está pronto para os testes
    - django_db_bloquer: Bloqueia o acesso ao banco para os testes
    """
    with django_db_blocker.unblock(): ## Desbloqueia o acesso ao banco 
        tenant, created = Client.objects.get_or_create(
            schema_name="public",
            defaults={"name": "Public"}
        )

        Domain.objects.get_or_create(
            domain="localhost",
            tenant=tenant,
            defaults={"is_primary": True}
        )

        if created:
            with schema_context(tenant.schema_name):
                call_command("seed_roles", verbosity=0)
                call_command("seed_group_permissions", verbosity=0)

    return tenant

@pytest.fixture
def tenant_client(tenant):
    from django_tenants.test.client import TenantClient
    return TenantClient(tenant)

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(tenant):
    from django_tenants.utils import schema_context
    from users.models import User
    with schema_context(tenant.schema_name):
        return User.objects.create(
            email="test@test.com",
            password="123456",
            first_name="Test",
            last_name="User"
        )
        
@pytest.fixture
def auth_client(tenant_client, user):
    from rest_framework_simplejwt.tokens import RefreshToken

    token = RefreshToken.for_user(user)
    tenant_client.defaults["HTTP_AUTHORIZATION"] = f"Bearer {token.access_token}"
    return tenant_client

pytest_plugins = [
    "tests.fixtures.user_fixture",
    "tests.fixtures.tenant_fixture"
]