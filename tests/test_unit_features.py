import pytest
from app.feature_engineering import stable_hash_bucket

def test_same_input_same_bucket():
    b1 = stable_hash_bucket("hello", 100)
    b2 = stable_hash_bucket("hello", 100)
    assert b1 == b2

def test_bucket_range():
    bucket = stable_hash_bucket("test", 10)
    assert 0 <= bucket < 10

def test_invalid_bucket_size():
    with pytest.raises(ValueError):
        stable_hash_bucket("x", 0)
def broken_function(
    pass
