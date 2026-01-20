from app.services.llm_service import stream_summary

def test_stream_parsing(monkeypatch):

    class FakeResp:
        def iter_lines(self):
            yield b'{"response":"Hello"}'
            yield b'{"response":" World"}'

    monkeypatch.setattr(
        "app.services.llm_service.requests.post",
        lambda *a, **k: FakeResp()
    )

    tokens = list(stream_summary("prompt"))

    assert tokens == ["Hello", " World"]
