# test_twttr.py
from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("12345") == "12345"

def test_empty_string():
    assert shorten("") == ""

def test_special_characters():
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"

def test_numbers():
    assert shorten("12345") == "12345"
