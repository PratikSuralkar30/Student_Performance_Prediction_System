import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Features defining based on the dataset
NUMERIC_FEATURES = [
    "Study Hours per Week", 
    "Attendance Rate", 
    "Previous Grades"
]
CATEGORICAL_FEATURES = [
    "Participation in Extracurricular Activities", 
    "Parent Education Level"
]

def get_preprocessing_pipeline():
    """
    Returns a scikit-learn ColumnTransformer for preprocessing 
    numeric and categorical features.
    """
    # Numeric pipeline: Impute missing values with median, then scale
    num_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    
    # Categorical pipeline: Impute with most frequent, then one-hot encode
    cat_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("ohe", OneHotEncoder(handle_unknown="ignore"))
    ])
    
    # Combine into a single ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_pipe, NUMERIC_FEATURES),
            ("cat", cat_pipe, CATEGORICAL_FEATURES)
        ]
    )
    
    return preprocessor

if __name__ == "__main__":
    print("Pipeline ready to be imported.")
