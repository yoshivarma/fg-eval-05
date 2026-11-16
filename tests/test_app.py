from src.app import make_slug


def test_slug():
    assert make_slug("Hello World") == "hello-world"
