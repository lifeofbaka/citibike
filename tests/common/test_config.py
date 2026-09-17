import pytest

from citibike_pipeline.common.config import (
    ensure_data_paths_exist,
    get_data_root,
    storage_layers,
)


def test_get_data_root_raises_when_unset(monkeypatch):
    monkeypatch.delenv("DATA_ROOT", raising=False)
    with pytest.raises(ValueError):
        get_data_root()


def test_get_data_root_returns_configured_path(monkeypatch, tmp_path):
    monkeypatch.setenv("DATA_ROOT", str(tmp_path))
    assert get_data_root() == tmp_path


def test_ensure_data_paths_exist_creates_all_layers(tmp_path):
    paths = ensure_data_paths_exist(data_root=tmp_path)

    assert set(paths) == set(storage_layers)
    for layer, path in paths.items():
        assert path == tmp_path / layer
        assert path.is_dir()


def test_ensure_data_paths_exist_is_idempotent(tmp_path):
    first = ensure_data_paths_exist(data_root=tmp_path)
    second = ensure_data_paths_exist(data_root=tmp_path)

    assert first == second
    for path in second.values():
        assert path.is_dir()


def test_ensure_data_paths_exist_falls_back_to_get_data_root(monkeypatch, tmp_path):
    monkeypatch.setenv("DATA_ROOT", str(tmp_path))

    paths = ensure_data_paths_exist()

    assert set(paths) == set(storage_layers)


def test_ensure_data_paths_exist_respects_custom_layers(tmp_path):
    paths = ensure_data_paths_exist(data_root=tmp_path, storage_layers=("custom",))

    assert set(paths) == {"custom"}
    assert (tmp_path / "custom").is_dir()
