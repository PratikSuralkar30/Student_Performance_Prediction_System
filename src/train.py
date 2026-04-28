import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from xgboost import XGBClassifier
from pipeline import get_preprocessing_pipeline
import matplotlib.pyplot as plt
import seaborn as sns

def train_model(data_path="data/simulated_student_data.csv", model_save_path="models/student_risk_model.joblib"):
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    
    # Target column processing (convert Yes/No to 1/0)
    # We want to predict if a student is "At Risk". 
    # Let's say "Passed" == 'No' means At Risk (1), "Passed" == 'Yes' means Not At Risk (0).
    df['At_Risk'] = (df['Passed'] == 'No').astype(int)
    
    # Drop target columns, carefully handling if Student ID exists
    cols_to_drop = ["Passed", "At_Risk"]
    if "Student ID" in df.columns:
        cols_to_drop.append("Student ID")
    
    X = df.drop(columns=cols_to_drop)
    y = df["At_Risk"]
    
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    
    print("Building pipeline...")
    preprocessor = get_preprocessing_pipeline()
    
    # We will use XGBoost as our classifier
    model = XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42,
        use_label_encoder=False,
        eval_metric="logloss"
    )
    
    # Create the full pipeline
    clf_pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", model)
    ])
    
    print("Training model...")
    clf_pipeline.fit(X_train, y_train)
    
    print("Evaluating model...")
    y_pred = clf_pipeline.predict(X_test)
    y_proba = clf_pipeline.predict_proba(X_test)[:, 1]
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC Score: {roc_auc_score(y_test, y_proba):.4f}")
    
    # Save the model
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    joblib.dump(clf_pipeline, model_save_path)
    print(f"Model saved successfully to {model_save_path}")
    
    # Generate Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Not At Risk', 'At Risk'], yticklabels=['Not At Risk', 'At Risk'])
    plt.title('Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/confusion_matrix.png")
    print("Confusion matrix plot saved to outputs/confusion_matrix.png")

if __name__ == "__main__":
    train_model()
