import pytest
from solutions.lc_1768_solution import mergeAlternately
def test_mergeAlternately():
    assert mergeAlternately("abc", "def") == "adbecf"
def test_mergeAlternately_longer_first():
    assert mergeAlternately("abc123", "def") == "adbecf123"
def test_mergeAlternately_longer_second():
    assert mergeAlternately("abc", "def12") == "adbecf12"