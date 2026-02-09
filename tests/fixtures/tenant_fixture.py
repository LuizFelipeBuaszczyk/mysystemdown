import pytest

@pytest.fixture
def tenant_post_data():
    """Payload base para o endpoint de criação de tenant"""
    return {
        "client": {
            "schema_name": "tenant_test",
            "name": "Tenant Test"
        },
        "domain": {
            "domain": "tenant_test.locahost"
        }
    }