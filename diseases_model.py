import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def predict_outcome(disease, fever, cough, fatigue, difficulty_breathing, age, gender, blood_pressure, cholesterol_level):
    df = pd.read_csv(r"C:\Users\surya\Downloads\Disease_symptom_and_patient_profile_dataset.csv")

    # Preprocess input data
    label_encoder = LabelEncoder()
    df['Disease'] = label_encoder.fit_transform(df['Disease'])
    # Encode the input values
    disease = label_encoder.transform([disease])[0]
    
    # Encode Gender
    gender_encodings = {'Male': 0, 'Female': 1}
    gender = gender_encodings[gender]

    # Assign numerical values for Blood Pressure
    blood_pressure_encodings = {'Low': 0, 'Normal': 1, 'High': 2}
    blood_pressure = blood_pressure_encodings[blood_pressure]

    # Assign numerical values for Cholesterol Level
    cholesterol_level_encodings = {'Low': 0, 'Normal': 1, 'High': 2}
    cholesterol_level = cholesterol_level_encodings[cholesterol_level]
    
    # Load the model
    X = df.drop('Outcome Variable', axis=1)
    y = df['Outcome Variable']
    clf = RandomForestClassifier()
    clf.fit(X, y)
    
    # Make prediction
    prediction = clf.predict([[disease, fever, cough, fatigue, difficulty_breathing, 
                                age, gender, blood_pressure, cholesterol_level]])[0]
    
    return prediction


# Streamlit app layout
st.title('Disease Outcome Predictor')

disease = st.selectbox('Select Disease', ['Influenza', 'Common Cold', 'Eczema', 'Asthma', 'Hyperthyroidism',
 'Allergic Rhinitis', 'Anxiety Disorders', 'Diabetes' ,'Gastroenteritis',
 'Pancreatitis', 'Rheumatoid Arthritis', 'Depression' ,'Liver Cancer',
 'Stroke', 'Urinary Tract Infection' ,'Dengue Fever' ,'Hepatitis',
 'Kidney Cancer' ,'Migraine', 'Muscular Dystrophy' ,'Sinusitis',
 'Ulcerative Colitis' ,'Bipolar Disorder' ,'Bronchitis', 'Cerebral Palsy',
 'Colorectal Cancer', 'Hypertensive Heart Disease' ,'Multiple Sclerosis',
 'Myocardial Infarction (Heart...' ,'Urinary Tract Infection (UTI)',
 'Osteoporosis' ,'Pneumonia' 'Atherosclerosis',
 'Chronic Obstructive Pulmonary...', 'Epilepsy' ,'Hypertension',
 'Obsessive-Compulsive Disorde...' ,'Psoriasis' ,'Rubella' ,'Cirrhosis',
 'Conjunctivitis (Pink Eye)', 'Liver Disease', 'Malaria' ,'Spina Bifida',
 'Kidney Disease', 'Osteoarthritis' ,'Klinefelter Syndrome', 'Acne',
 'Brain Tumor', 'Cystic Fibrosis' ,'Glaucoma', 'Rabies', 'Chickenpox',
 'Coronary Artery Disease', 'Eating Disorders (Anorexia,...', 'Fibromyalgia',
 'Hemophilia', 'Hypoglycemia' ,'Lymphoma', 'Tuberculosis' ,'Lung Cancer',
 'Hypothyroidism', 'Autism Spectrum Disorder (ASD)', "Crohn's Disease",
 'Hyperglycemia', 'Melanoma', 'Ovarian Cancer', 'Turner Syndrome',
 'Zika Virus', 'Cataracts' ,'Pneumocystis Pneumonia (PCP)', 'Scoliosis',
 'Sickle Cell Anemia' ,'Tetanus', 'Anemia' ,'Cholera' ,'Endometriosis',
 'Sepsis' 'Sleep Apnea' ,'Down Syndrome', 'Ebola Virus', 'Lyme Disease',
 'Pancreatic Cancer' ,'Pneumothorax', 'Appendicitis' ,'Esophageal Cancer',
 'HIV/AIDS' 'Marfan Syndrome' ,"Parkinson's Disease", 'Hemorrhoids',
 'Polycystic Ovary Syndrome (PCOS)', 'Systemic Lupus Erythematosus...',
 'Typhoid Fever' ,'Breast Cancer', 'Measles' ,'Osteomyelitis' ,'Polio',
 'Chronic Kidney Disease' ,'Hepatitis B', 'Prader-Willi Syndrome',
 'Thyroid Cancer', 'Bladder Cancer' ,'Otitis Media (Ear Infection)',
 'Tourette Syndrome' ,"Alzheimer's Disease",
 'Chronic Obstructive Pulmonary Disease (COPD)' ,'Dementia',
 'Diverticulitis' ,'Mumps', 'Cholecystitis' ,'Prostate Cancer',
 'Schizophrenia', 'Gout' ,'Testicular Cancer', 'Tonsillitis',
 'Williams Syndrome'])
fever = st.radio('Fever no-0 yes-1', [0, 1])
cough = st.radio('Cough no-0 yes-1', [0, 1])
fatigue = st.radio('Fatigue no-0 yes-1', [0, 1])
difficulty_breathing = st.radio('Difficulty Breathing no-0 yes-1', [0, 1])
age = st.slider('Age', 0, 100)
gender = st.selectbox('Gender', ['Male', 'Female'])
blood_pressure = st.selectbox('Blood Pressure', ['Low', 'Normal', 'High'])
cholesterol_level = st.selectbox('Cholesterol Level', ['Low', 'Normal', 'High'])

if st.button('Predict Outcome'):
    st.write(f'The predicted outcome for the patient is: Positive')
else:
    print("The predicted outcome for the patient is: Negative.")