def test_ingest_starts(client, monkeypatch):
    # 1) Mock news fetch
    monkeypatch.setattr(
        "app.api.routers.ingest.fetch_crypto_news",
        lambda: []
    )

    # 2) Mock Qdrant write so background task does nothing
    monkeypatch.setattr(
        "app.api.routers.ingest.upsert_articles",
        lambda x: 0
    )

    r = client.post("/ingest/news")

    assert r.status_code == 200
    assert r.json()["status"] == "started"
