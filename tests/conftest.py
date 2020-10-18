import pytest
from ramp_assessment import create_app
from ramp_assessment.transform.service import TransformService

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def service():
    return TransformService()