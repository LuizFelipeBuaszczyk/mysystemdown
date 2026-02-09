import pytest
from tests.factories.system_factory import SystemFactory
from django_tenants.utils import schema_context

@pytest.fixture
def system():
    return SystemFactory.build()

@pytest.fixture
def systems():
    return SystemFactory.build_batch(size=3)

@pytest.fixture
def system_post_data():
    return {
        "name": "System 1",
        "description": "System 1 description"
    }