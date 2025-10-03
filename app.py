import streamlit as st
import pandas as pd
from pkgs.st_functions import textMarkdown, selectbox, numericalDataInput, figure_set
import pickle
from pkgs.visualization_functions import locationCountPlot, agehistPlot,exercisePiePlot, bloodSugerPiePlot, slopCountPlot, restingElectroCountPlot, genderCountPlot,chestingPainCountPlot
#############################################
with open(r'models\best_model_LR.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
textMarkdown('Heart Diseases Diagnosis System', '38px', "#078B0C")
# Categorical Data
genderType = selectbox('Gender type', 'sex', 'gender_selectbox') 
chest_pain = selectbox('Chest Pain type', 'chest_pain', 'chest_pain_selectbox') 
fasting_blood_sugar = selectbox('Fasting Blood Sugar', 'fasting_blood_sugar', 'blood_suger_selectbox')
resting_electrocardiographic = selectbox('Resting Electrocardiographic', 'resting_electrocardiographic_results','resting_electro_selectbox')
exercise_induced_angina = selectbox('Exercise Induced Angina', 'exercise_induced_angina', 'exercise_induced_selectbox')
slope = selectbox('Slope', 'slope', 'slop_selectbox')

# Numerical Data
age = numericalDataInput('Enter Paient Age MedicalRange(5:95) year',5.0,95.0,5.0)
blood_pressure = numericalDataInput('Enter Paient resting Blood Pressure MedicalRange(90:200) mmHg',90.0,200.0,90.0)
cholesterol = numericalDataInput('Enter Paient Cholesterol MedicalRange(80:564) mg/dL',80.0,564.0,80.0)
heart_rate = numericalDataInput('Enter Paient Max heart rate achieved MedicalRange(70:202) bpm',70.0,202.0,70.0)
oldpeak = numericalDataInput('Enter Paient OldPeak MedicalRange(0:6.2) mm',0.0,6.2,0.0)
####
if st.button('Paient Diagnosis'):
    new_data = pd.DataFrame({
        'sex':[genderType],
        'chest_pain':[chest_pain],
        'fasting_blood_sugar':[fasting_blood_sugar],
        'resting_electrocardiographic_results':[resting_electrocardiographic],
        'exercise_induced_angina':[exercise_induced_angina],
        'slope':[slope],
        'age':[age],
        'resting_systolic_blood_pressure':[blood_pressure],
        'cholesterol':[cholesterol],
        'max_heart_rate_achieved':[heart_rate],
        'oldpeak':[oldpeak]
    })
    finial_prediction = model.predict(new_data)[0]
    if finial_prediction == 1:
        textMarkdown('The patient exhibits indications of cardiac pathology, necessitating consultation with a specialist physician.','18px', "#F5330C") #st.header(f'The patient exhibits indications of cardiac pathology, necessitating consultation with a specialist physician.')
    elif finial_prediction == 0:
        textMarkdown('The assessment indicates no evidence of cardiac pathology; ongoing medical vigilance and specialist consultation are nevertheless recommended.','18px', "#23EC2A")#st.header(f'The assessment indicates no evidence of cardiac pathology; ongoing medical vigilance and specialist consultation are nevertheless recommended.')
    else:
        st.warning(f'No Comment!!?')



#Data visualization
textMarkdown('Dataset analysis and visualization', '30px', "#1983F5")

if st.button('Dataset Analysis'):
    figure_set(locationCountPlot)
    figure_set(agehistPlot)
    figure_set(genderCountPlot)
    figure_set(exercisePiePlot)
    figure_set(bloodSugerPiePlot)
    figure_set(slopCountPlot)
    figure_set(restingElectroCountPlot)
    figure_set(chestingPainCountPlot)
    


