# Disease Outcome Predictor

A Streamlit web application that predicts the health outcome of patients based on disease type, symptoms, demographic, and health indicators using a Random Forest classifier.

## Overview

This web application allows users to input patient-specific information, including disease, symptoms (fever, cough, fatigue, difficulty breathing), age, gender, blood pressure, and cholesterol level. It processes these inputs, applies necessary preprocessing and encoding, and predicts the patient’s outcome using a trained Random Forest model on a disease symptom and patient profile dataset.

## Features

- Select from a comprehensive list of diseases.
- Input symptoms and demographic data via an interactive UI.
- Automatic encoding of categorical variables.
- Real-time prediction of patient outcome using a machine learning model.
- Built with Python, Streamlit, and scikit-learn.

## Dataset

The model uses a CSV dataset named `disease_dataset.csv` containing patient profiles, symptoms, diseases, and outcome variables.

## Working

- The model is trained each time a prediction is made, which might affect performance.
- Categorical variables like gender, blood pressure, and cholesterol levels are manually encoded.
- Ensure input values match expected formats to avoid runtime errors.

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn (Random Forest Classifier)

