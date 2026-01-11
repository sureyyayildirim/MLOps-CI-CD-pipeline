import time
import requests

BASE = "http://localhost:8000"

def wait_for_ready(timeout_s: int = 20) -> None:
    start = time.time()
    while time.time() - start < timeout_s:
        try:
            r = requests.get(f"{BASE}/health", timeout=2)
            if r.status_code == 200:
                return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError("Service did not become ready in time")

def main() -> None:
    wait_for_ready()

    r = requests.post(f"{BASE}/predict", json={"text": "hello"}, timeout=5)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}: {r.text}"

    data = r.json()
    assert "bucket" in data, f"Response missing 'bucket': {data}"

    print("SMOKE OK:", data)

if __name__ == "__main__":
    main()
