import os
import pandas as pd
import requests
from src.config import DATA_URL, RAW_DATA_PATH

def download_data():
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)
    resp = requests.get(DATA_URL)
    resp.raise_for_status()
    with open(RAW_DATA_PATH, "wb") as f:
        f.write(resp.content)

def load_data():
    df = pd.read_csv(RAW_DATA_PATH, header=None)
    return df

if __name__ == "__main__":
    download_data()
    print("Data downloaded to", RAW_DATA_PATH)
