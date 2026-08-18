from greet import greet


def test_greet_includes_name():
    assert "Ada" in greet("Ada")


def test_greet_full_message():
    assert greet("Ada") == "Hello, Ada! Welcome to your first pull request."
