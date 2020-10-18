import pytest
from ramp_assessment import create_app
from ramp_assessment.multiply.service import MultiplyService

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def service():
    return MultiplyService()