from app.services.normalizer import normalize_article

def test_normalizer_defaults():
    raw = {
        "title": "BTC",
        "content": None,
        "publishedAt": "2024-01-01"
    }

    n = normalize_article(raw)

    assert n["content"] == ""
    assert "id" in n
    assert n["title"] == "BTC"
