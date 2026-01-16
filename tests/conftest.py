import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="session")
def client():
    return TestClient(app)

import pytest
import uuid

@pytest.fixture
def sample_article():
    return {
        "id": str(uuid.uuid4()),
        "title": "Bitcoin ETF inflows rise",
        "content": "Institutions bought more BTC today",
        "sentiment": "bullish",
        "vector": [0.1] * 768
    }
