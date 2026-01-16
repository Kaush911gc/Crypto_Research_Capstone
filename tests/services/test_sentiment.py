def test_sentiment(monkeypatch):
    class Fake:
        def json(self):
            return {"response": "bearish"}
        def raise_for_status(self):
            pass

    monkeypatch.setattr(
        "app.services.sentiment_service.requests.post",
        lambda *a, **k: Fake()
    )

    from app.services.sentiment_service import classify_sentiment
    assert classify_sentiment("x") == "bearish"
