from utils import to_roman, from_roman

def test_roman():
    assert to_roman(2025) == "MMXXV"
    assert to_roman(1984) == "MCMLXXXIV"
    assert from_roman("MCMLXXXIV") == 1984
    assert from_roman("MMXXV") == 2025
