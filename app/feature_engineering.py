import hashlib

def stable_hash_bucket(text: str, num_buckets: int = 100) -> int:
    """
    Deterministic hashing -> bucket id [0, num_buckets-1]
    """
    if num_buckets <= 0:
        raise ValueError("num_buckets must be > 0")

    digest = hashlib.md5(text.encode("utf-8")).hexdigest()
    as_int = int(digest, 16)
    return as_int % num_buckets
