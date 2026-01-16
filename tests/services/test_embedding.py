def test_embedding(monkeypatch):
    class Fake:
        def json(self):
            return {"embedding": [0.2] * 384}
        def raise_for_status(self):
            pass

    monkeypatch.setattr(
        "app.services.embedding_service.requests.post",
        lambda *a, **k: Fake()
    )

    from app.services.embedding_service import embed_text
    vec = embed_text("btc")

    assert len(vec) == 384
