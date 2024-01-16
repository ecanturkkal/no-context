import pytest
from fastapi.testclient import TestClient
from src.main import get_application


@pytest.fixture(scope="session")
def test_client():
    client = TestClient(get_application())
    yield client
