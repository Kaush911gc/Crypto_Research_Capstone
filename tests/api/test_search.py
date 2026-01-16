def test_search(client, monkeypatch):

    fake_results = [{
        "title": "BTC",
        "content": "Up",
        "sentiment": "bullish",
        "score": 0.6
    }]

    # 🔥 PATCH WHERE ROUTER USES IT
    monkeypatch.setattr(
        "app.api.routers.query.semantic_search",
        lambda q, k: fake_results
    )

    r = client.post("/query/search", json={
        "query": "bitcoin",
        "top_k": 5
    })

    data = r.json()

    assert r.status_code == 200
    assert "results" in data
    assert data["results"][0]["title"] == "BTC"
