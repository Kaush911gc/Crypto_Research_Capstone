from app.services.summary_prompt import build_summary_prompt

def test_prompt_contains_sections():
    articles = [
        {"title": "BTC", "content": "Up", "sentiment": "bullish"},
        {"title": "ETH", "content": "Down", "sentiment": "bearish"},
    ]

    prompt = build_summary_prompt("bitcoin", articles)

    assert "User query" in prompt
    assert "BTC" in prompt
    assert "ETH" in prompt
    assert "bullish" in prompt

def test_prompt_empty_articles():
    from app.services.summary_prompt import build_summary_prompt

    p = build_summary_prompt("btc", [])

    assert "No articles" in p or "0" in p
