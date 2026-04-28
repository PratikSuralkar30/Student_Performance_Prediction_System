from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from pydantic import BaseModel
import os

app = FastAPI(title="Student Risk Prediction API")

# Configure CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'student_risk_model.joblib')
model = None

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print("Model loaded successfully.")
    else:
        print("Model not found! Run 'python src/train.py' first.")

# Define input data schema
class StudentData(BaseModel):
    study_hours: float
    attendance: float
    prev_grades: float
    activities: str
    parent_edu: str

@app.post("/predict")
def predict(data: StudentData):
    if model is None:
        return {"error": "Model not loaded on the server."}
    
    # Create DataFrame from input
    input_df = pd.DataFrame([[
        data.study_hours, 
        data.attendance, 
        data.prev_grades, 
        data.activities, 
        data.parent_edu
    ]], columns=[
        'Study Hours per Week', 
        'Attendance Rate', 
        'Previous Grades', 
        'Participation in Extracurricular Activities', 
        'Parent Education Level'
    ])
    
    # Predict
    # 1 is At Risk, 0 is Not At Risk (from our train.py)
    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][prediction])
    
    return {
        "prediction": prediction,
        "is_at_risk": prediction == 1,
        "confidence": probability,
        "message": "Student is at risk" if prediction == 1 else "Student is not at risk"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
