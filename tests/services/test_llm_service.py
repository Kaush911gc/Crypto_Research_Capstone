from app.services.llm_service import stream_summary
from app.services.llm_service import summarize_articles

class FakeResp:
    def __init__(self, text):
        self._text = text

    def raise_for_status(self):
        pass

    def json(self):
        return {"response": self._text}


def test_summarize_articles_basic(monkeypatch):
    monkeypatch.setattr(
        "app.services.llm_service.requests.post",
        lambda *a, **k: FakeResp(
            "Here are results\n- A\n- B\nsummary end"
        )
    )

    out = summarize_articles(
        "btc",
        [{"title": "T1", "content": "C1"}]
    )

    # cleaning should remove intro lines
    assert "Here are" not in out
    assert "- A" in out
    assert "- B" in out


def test_summarize_articles_empty(monkeypatch):
    monkeypatch.setattr(
        "app.services.llm_service.requests.post",
        lambda *a, **k: FakeResp("summary")
    )

    out = summarize_articles("btc", [])
    assert isinstance(out, str)

class FakeStream:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        pass

    def iter_lines(self):
        yield b"token1"
        yield b"token2"


def test_stream_summary(monkeypatch):
    monkeypatch.setattr(
        "app.services.llm_service.requests.post",
        lambda *a, **k: FakeStream()
    )

    tokens = list(stream_summary("hi"))
    assert tokens == ["token1", "token2"]
