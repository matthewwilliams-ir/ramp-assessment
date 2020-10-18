import pytest
from ramp_assessment import create_app

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()