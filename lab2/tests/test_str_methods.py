import pytest

def test_capitalize():
    assert "hello".capitalize() == "Hello"

def test_islower():
    assert "hello".islower() is True
    assert "Hello".islower() is False

def test_isidentifier():
    assert "variable".isidentifier() is True
    assert "123variable".isidentifier() is False

def test_endswith():
    assert "hello".endswith("lo") is True
    assert "hello".endswith("he") is False

def test_upper():
    assert "hello".upper() == "HELLO"

def test_join():
    assert " ".join(["hello", "world"]) == "hello world"

def test_replace():
    assert "hello world".replace("world", "there") == "hello there"

def test_isupper():
    assert "HELLO".isupper() is True
    assert "Hello".isupper() is False

def test_isnumeric():
    assert "123".isnumeric() is True
    assert "123a".isnumeric() is False

def test_startswith():
    assert "hello".startswith("he") is True
    assert "hello".startswith("lo") is False

def test_lower():
    assert "HELLO".lower() == "hello"

def test_split():
    assert "hello world".split() == ["hello", "world"]

def test_swapcase():
    assert "Hello".swapcase() == "hELLO"

def test_count():
    assert "hello".count("l") == 2

def test_isdigit():
    assert "123".isdigit() is True
    assert "123a".isdigit() is False
