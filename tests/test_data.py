import os
from src.data_download import download_data, load_data
from src.config import RAW_DATA_PATH

def test_download_data():
    # Ensure file downloads correctly
    download_data()
    assert os.path.exists(RAW_DATA_PATH)

def test_load_data():
    df = load_data()
    assert df is not None
    assert df.shape[0] > 0
    assert df.shape[1] > 0
