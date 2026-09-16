import os 
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


# Storage layers and their corresponding paths
storage_layers = ('bronze', 'silver', 'gold')


def get_data_root() -> Path:
    """
    Returns the root path for data storage, either from the environment variable 'DATA_ROOT' 
    """
    data_root = os.getenv('DATA_ROOT')
    if not data_root:
        raise ValueError("DATA_ROOT environment variable is not set.")
    return Path(data_root)

def ensure_data_paths_exist(data_root: Path | None = None, storage_layers: tuple[str,...] = storage_layers) -> dict[str, Path]:
    """
    Ensures that the data paths for the specified storage layers exist. 
    If they don't exist, they will be created.

    Args:
        data_root (Path): The root path for data storage.
        storage_layers (tuple): A tuple of storage layer names.

    Returns:
        dict: A dictionary mapping each storage layer to its corresponding path.
    """
    data_path = data_root or get_data_root()
    data_path.mkdir(parents=True, exist_ok=True)

    storage_paths = {}
    for layer in storage_layers:
        layer_path = data_path / layer
        layer_path.mkdir(parents=True, exist_ok=True) # create the directory if it doesn't exist
        storage_paths[layer] = layer_path
    return storage_paths


