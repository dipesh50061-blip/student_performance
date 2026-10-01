# Student Performance Analysis & Prediction

A Machine Learning project focused on analyzing student performance using *Exploratory Data Analysis (EDA)* and building a classification model to predict student performance.

The project uses a dataset of *4,000 student records* and explores how factors such as study hours, attendance, previous scores, and other student-related attributes relate to final academic performance.

---

## Project Overview

The main objectives of this project are:

- Understand the student performance dataset
- Perform data cleaning and preprocessing
- Analyze important patterns using EDA
- Study relationships between academic factors and final scores
- Analyze correlations between numerical features
- Build and evaluate Machine Learning classification models
- Save the final trained model
- Create an interactive Streamlit application for prediction

---

## Dataset

*Dataset:* student_performance_4000.csv

The dataset contains *4,000 student records* and *17 features*.

### Features

| Feature | Description |
|---|---|
| student_id | Unique identifier of the student |
| gender | Gender of the student |
| age | Age of the student |
| study_hours | Number of hours spent studying |
| attendance | Student attendance percentage |
| previous_score | Previous academic score |
| assignments_completed | Number of assignments completed |
| sleep_hours | Average number of hours slept |
| internet_access | Availability of internet access |
| parent_education | Education level of parents |
| extra_activities | Participation in extracurricular activities |
| family_income | Family income category |
| class_participation | Level of classroom participation |
| study_method | Study method used by the student |
| stress_level | Student stress level |
| final_score | Final academic score |
| performance | Target variable representing student performance |

### Target Variable

The target variable is:

text
performance


It represents the student's overall performance category.

---

## Exploratory Data Analysis

The EDA is divided into *Univariate, Bivariate, and Multivariate Analysis*.

### 1. Univariate Analysis

The following individual variable distributions are analyzed:

- *Target Distribution* — Distribution of the performance target variable.
- *Final Score Distribution* — Distribution of students' final_score.

### 2. Bivariate Analysis

The following relationships between two variables are analyzed:

- *Study Hours vs Final Score*
- *Attendance vs Final Score*
- *Previous Score vs Final Score*
- *Performance vs Study Hours*
- *Performance vs Attendance*

These analyses help understand relationships between important academic factors and student performance.

### 3. Multivariate Analysis

Only *correlation analysis* is performed for multivariate analysis.

This includes:

- Correlation matrix
- Correlation heatmap

The correlation analysis helps identify the strength and direction of relationships between numerical variables.

---

## Machine Learning

The project treats student performance prediction as a *multi-class classification problem*.

The target variable is:

text
performance


The Machine Learning workflow includes:

1. Data preprocessing
2. Feature selection
3. Encoding categorical variables
4. Train-test split
5. Model training
6. Model evaluation
7. Model comparison
8. Final model selection
9. Saving the trained model

### Models

Different classification algorithms are evaluated to determine their performance on the dataset.

The final trained model is saved as:

text
models/student_performance_model.pkl


---

## Model Evaluation

The models are evaluated using the following classification metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Macro F1 Score
- Confusion Matrix
- Classification Report

*Macro F1 Score* is considered an important evaluation metric because this is a multi-class classification problem and it gives equal importance to each class.

---

## Prediction

The trained model is used to predict student performance based on student-related attributes.

The prediction workflow is:

text
Student Input
      ↓
Data Preprocessing
      ↓
Trained ML Model
      ↓
Prediction
      ↓
Student Performance


The prediction logic is implemented in:

text
src/predict.py


---

## Streamlit Application

The project includes an interactive *Streamlit application* for student performance prediction.

Users can enter student information and obtain a predicted performance category.

The main application file is:

text
app.py


Run the application using:

bash
streamlit run app.py


---

## Project Structure

text
student-performance/
│
├── data/
│   └── student_performance_4000.csv
│
├── models/
│   └── student_performance_model.pkl
│
├── notebooks/
│   ├── student_performance_eda.ipynb
│   └── modeling.ipynb
│
├── src/
│   └── predict.py
│
├── app.py
├── README.md
└── requirements.txt


### Folder & File Description

- *data/* — Contains the student performance dataset.
- *models/* — Contains the trained Machine Learning model.
- *notebooks/student_performance_eda.ipynb* — Contains data exploration, cleaning, and EDA.
- *notebooks/modeling.ipynb* — Contains preprocessing, model training, evaluation, and final model selection.
- *src/predict.py* — Contains the prediction functionality used by the application.
- *app.py* — Main Streamlit application.
- *requirements.txt* — Contains all required Python libraries.
- *README.md* — Project documentation.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook
- VS Code
- Conda
- Git & GitHub

---

## Installation

### 1. Clone the Repository

bash
git clone <your-repository-url>


Navigate to the project directory:

bash
cd student-performance


### 2. Create a Conda Environment

bash
conda create -n student-performance python=3.11


Activate the environment:

bash
conda activate student-performance


### 3. Install Dependencies

bash
pip install -r requirements.txt


---

## Running the Project

### Run EDA Notebook

Open:

text
notebooks/student_performance_eda.ipynb


Run the notebook to perform the exploratory data analysis.

### Run Modeling Notebook

Open:

text
notebooks/modeling.ipynb


Run the notebook to train and evaluate the Machine Learning models.

### Run Streamlit Application

From the project root directory:

bash
streamlit run app.py


The application will open in your default web browser.

---

## Machine Learning Workflow

text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Preparation
   ↓
Data Preprocessing
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Comparison
   ↓
Final Model
   ↓
Save Model
   ↓
Streamlit Prediction App


---

## Key Questions Explored

This project explores the following questions:

- How is student performance distributed?
- How is the final score distributed?
- Is study time associated with final scores?
- Is attendance associated with final scores?
- Is previous academic performance associated with final scores?
- How does study time vary across performance categories?
- How does attendance vary across performance categories?
- What relationships exist between numerical variables?

---

## Future Improvements

Possible future improvements include:

- Hyperparameter tuning
- Cross-validation
- Feature importance analysis
- Model explainability
- Improved Streamlit dashboard
- Model performance monitoring
- Cloud deployment
- API integration using FastAPI

---

## Author

**Depesh Kumar**  
**AI Engineer Intern**

---

## License

This project is created for *educational and portfolio purposes*.