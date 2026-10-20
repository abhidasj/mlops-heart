import mlflow
import mlflow.sklearn
import pickle

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

from src.data_download import load_data
from src.preprocess import build_preprocessor
from src.config import MODEL_PATH, MLFLOW_EXPERIMENT

def train():
    df = load_data()
    preprocessor, X, y = build_preprocessor(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier(
        n_estimators=200,
        max_depth=5,
        random_state=42
    )

    pipe = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("model", clf)
    ])

    mlflow.set_experiment(MLFLOW_EXPERIMENT)
    with mlflow.start_run():
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)
        y_proba = pipe.predict_proba(X_test)[:, 1]

        acc = accuracy_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_proba)

        mlflow.log_param("n_estimators", 200)
        mlflow.log_param("max_depth", 5)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("roc_auc", auc)

        mlflow.sklearn.log_model(pipe, "model")

        with open(MODEL_PATH, "wb") as f:
            pickle.dump(pipe, f)

        print(f"Accuracy: {acc:.3f}, ROC-AUC: {auc:.3f}")

if __name__ == "__main__":
    train()
