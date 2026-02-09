import pytest

@pytest.fixture
def service_post_data():
    return {
        "title": "Service 1",
        "url": "http://localhost.com",
        "description": "Service 1 description",
        "health_check_interval": 60
    }