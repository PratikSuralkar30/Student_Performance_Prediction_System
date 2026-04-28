import pandas as pd
import numpy as np
import os

def generate_mock_data(n=2000):
    print("Generating simulated student data...")
    np.random.seed(42)
    
    # 1. Generate Base Features
    study_hours = np.random.normal(15, 8, n)
    attendance = np.random.normal(80, 20, n)
    prev_grades = np.random.normal(70, 15, n).clip(0, 100)
    
    # Categorical Features
    activities = np.random.choice(['Yes', 'No'], n, p=[0.4, 0.6])
    parent_edu = np.random.choice(['High School', 'Bachelor', 'Master'], n, p=[0.5, 0.3, 0.2])
    
    # 2. Apply Mathematical Correlation (The fix for your 53% accuracy)
    score = (np.abs(study_hours) * 1.5) + (np.clip(attendance, 0, 100) * 0.5) + (prev_grades * 0.5)
    passed = np.where(score > np.median(score), 'Yes', 'No')
    
    # 3. Introduce Intentional "Dirty" Data for your Resume
    study_hours[::10] = -np.abs(study_hours[::10]) # Inject negative study hours
    attendance[::15] = attendance[::15] + 30       # Inject attendance > 100%
    
    # 4. Create DataFrame
    df = pd.DataFrame({
        'Study Hours per Week': study_hours,
        'Attendance Rate': attendance,
        'Previous Grades': prev_grades,
        'Participation in Extracurricular Activities': activities,
        'Parent Education Level': parent_edu,
        'Passed': passed
    })
    
    # Inject missing values
    df.loc[np.random.choice(df.index, 50), 'Previous Grades'] = np.nan
    
    # Save it
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/simulated_student_data.csv', index=False)
    print("Success! Simulated data saved to data/simulated_student_data.csv")

if __name__ == "__main__":
    generate_mock_data()