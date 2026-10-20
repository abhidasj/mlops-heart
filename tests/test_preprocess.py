import pandas as pd
from src.data_download import load_data
from src.preprocess import build_preprocessor

def test_preprocessor_shapes():
    df = load_data()
    preprocessor, X, y = build_preprocessor(df)

    # X and y must have same number of rows
    assert X.shape[0] == y.shape[0]

def test_preprocessor_output():
    df = load_data()
    preprocessor, X, y = build_preprocessor(df)

    # Fit the preprocessor and transform
    X_transformed = preprocessor.fit_transform(X)

    # Output must not be empty
    assert X_transformed.shape[0] > 0
    assert X_transformed.shape[1] > 0
