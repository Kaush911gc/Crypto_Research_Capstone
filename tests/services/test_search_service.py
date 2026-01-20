from app.services.search_service import semantic_search

class FakeResponse:
    def __init__(self):
        self.points = [
            type("p", (), {
                "score": 0.8,
                "payload": {"title": "BTC"}
            })
        ]

class FakeClient:
    def query_points(self, **k):
        return FakeResponse()

def test_semantic_mapping(monkeypatch):
    monkeypatch.setattr(
        "app.services.search_service.get_qdrant_client",
        lambda: FakeClient()
    )

    res = semantic_search([0.1]*768, 5)

    assert res[0]["title"] == "BTC"
    assert res[0]["score"] == 0.8
