import pandas as pd
import joblib

model = joblib.load(
    "D:\EDA projects\student_performance\models\student_performance_model.pkl"
)

student = pd.DataFrame({
    "gender": ["Male"],
    "age": [18],
    "study_hours": [5.0],
    "attendance": [90.0],
    "previous_score": [78.0],
    "assignments_completed": [12],
    "sleep_hours": [7.0],
    "internet_access": ["Yes"],
    "parent_education": ["Graduate"],
    "extra_activities": ["Yes"],
    "family_income": ["Medium"],
    "class_participation": [8],
    "study_method": ["Self Study"],
    "stress_level": [4]
})

prediction = model.predict(student)

print("Predicted Performance:", prediction[0])