def test_upsert_format(monkeypatch, sample_article):

    called = {}

    class FakeClient:
        def upsert(self, collection_name, points):
            called["collection"] = collection_name
            called["points"] = points

    # --- PATCH THE FACTORY ---
    monkeypatch.setattr(
        "app.db.qdrant.get_qdrant_client",
        lambda: FakeClient()
    )

    from app.db.qdrant import upsert_articles, COLLECTION_NAME

    result = upsert_articles([sample_article])

    # ---- ASSERTIONS ----
    assert result == 1
    assert called["collection"] == COLLECTION_NAME

    point = called["points"][0]


    assert point.id == sample_article["id"]
    assert point.vector == sample_article["vector"]

    assert "vector" not in point.payload
    assert "id" not in point.payload
    assert point.payload["title"] == sample_article["title"]
