import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="session")
def test_client():
    client = TestClient(app)
    yield client
