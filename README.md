# 🎓 Student Performance Prediction System

![Student Performance System](https://img.shields.io/badge/Machine_Learning-Python-blue)
![XGBoost](https://img.shields.io/badge/Algorithm-XGBoost-orange)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![Next.js](https://img.shields.io/badge/Frontend-Next.js-black)

An end-to-end Machine Learning project to predict student performance and identify "at-risk" students early using past academic, behavioral, and demographic data. This project acts as a perfect template for EdTech analytics and demonstrates industry-standard ML pipelines.

## 🚀 Project Overview
Educational institutions need to identify students who are likely to fail so that they can provide early interventions (like tutoring or advisory meetings). 

This project uses **XGBoost Classifier** combined with a robust **Scikit-Learn Preprocessing Pipeline** to predict the likelihood of a student being "At Risk", deployed behind an interactive **Next.js Dashboard** with a **FastAPI** backend.

### Key Features
- **Scikit-Learn Pipeline**: Prevents data leakage with built-in One-Hot Encoding and Standard Scaling.
- **XGBoost Model**: Highly accurate and robust industry-standard algorithm.
- **FastAPI Backend**: Fast, asynchronous Python API serving the ML model.
- **Next.js Web App**: A beautiful, interactive React UI for educators to input student data and get real-time risk assessments.
- **Actionable Insights**: Recommends next steps based on model confidence.

## 📂 Folder Structure
```text
Student-Performance-Prediction/
├── data/
│   └── student_performance_prediction.csv  # Dataset
├── models/
│   └── student_risk_model.joblib           # Trained Model
├── src/
│   ├── pipeline.py                         # Preprocessing logic
│   └── train.py                            # Model training script
├── outputs/                                # Generated artifacts
├── serving/
│   └── app.py                              # FastAPI backend
├── web/                                    # Next.js frontend
└── requirements.txt                        # Python dependencies
```

## 💻 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/Student-Performance-Prediction.git
cd Student-Performance-Prediction
```

2. **Backend Setup**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate # Mac/Linux
pip install -r requirements.txt
```

3. **Frontend Setup**
```bash
cd web
npm install
```

## 🧠 Training the Model

Before running the web app, you must train the model and generate the `.joblib` file:

```bash
python src/train.py
```
*This will print the Classification Report, ROC-AUC score, and save a Confusion Matrix in `outputs/`.*

## 🌐 Running the Web Application

1. **Start the FastAPI server:**
```bash
# In the root project directory with virtual environment activated
python serving/app.py
```

2. **Start the Next.js frontend:**
```bash
# Open a new terminal, navigate to the web directory
cd web
npm run dev
```

Your browser will automatically open or you can navigate to `http://localhost:3000`.

## 📊 Sample Visualizations
*(Note: Once you run `train.py`, add your confusion matrix screenshot here by saving it to the `images/` folder and linking it!)*
- `images/app_screenshot.png`
- `images/confusion_matrix.png`

---
*Developed for Data Science Portfolio | Open Source & Beginner Friendly*
