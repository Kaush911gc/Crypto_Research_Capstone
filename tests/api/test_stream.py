def test_stream(client, monkeypatch):

    # ---- MOCK SEARCH ----
    monkeypatch.setattr(
        "app.api.routers.query.semantic_search",
        lambda q, k: [{
            "title": "BTC",
            "content": "Up",
            "sentiment": "bullish"
        }]
    )

    # ---- MOCK PROMPT ----
    monkeypatch.setattr(
        "app.api.routers.query.build_summary_prompt",
        lambda payload, articles: "prompt"
    )

    # ---- MOCK LLM STREAM ----
    def fake_stream(prompt):
        yield "token1"
        yield " token2"

    monkeypatch.setattr(
        "app.api.routers.query.stream_summary",
        fake_stream
    )

    r = client.post("/query/stream-summary", json={
        "query": "btc",
        "top_k": 3
    })

    assert r.status_code == 200
    assert "token1" in r.text
