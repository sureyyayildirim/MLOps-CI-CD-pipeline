from app.model import load_metadata

def test_load_metadata_from_file(tmp_path):
    metadata_file = tmp_path / "metadata.json"
    metadata_file.write_text(
        '{"model_version": "x", "feature_space": 42}',
        encoding="utf-8"
    )

    data = load_metadata(str(metadata_file))

    assert data["model_version"] == "x"
    assert data["feature_space"] == 42
