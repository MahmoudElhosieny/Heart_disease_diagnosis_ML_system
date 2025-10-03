# Data analysis libraries
import pandas as pd
from pkgs.data import row_data

pd.set_option('future.no_silent_downcasting', True)
rowData = row_data
data = rowData.drop(columns = ['id'])
# Data Exploration
# print(data.sample(3))
# print(data['dataset'].unique())
# print(data['cp'].unique())
data = data.rename(columns = {'dataset':'dataset_location','cp':'chest_pain','trestbps':'resting_systolic_blood_pressure','chol':'cholesterol','fbs':'fasting_blood_sugar','restecg':'resting_electrocardiographic_results','thalch':'max_heart_rate_achieved',
                       'exang':'exercise_induced_angina', 'ca':'coronary_angiography'})
# print(data.sample(2))
# print(data['num'].unique())
# print((data.isnull().sum()/data.shape[0])*100)
data['resting_systolic_blood_pressure']= data['resting_systolic_blood_pressure'].fillna(data['resting_systolic_blood_pressure'].median())
data['cholesterol']= data['cholesterol'].fillna(data['cholesterol'].median())
data['fasting_blood_sugar']= data['fasting_blood_sugar'].fillna(data['fasting_blood_sugar'].mode())
data.drop(columns = ['coronary_angiography'], axis = 1) # Null values is more than 60% of data, so, we delete the column
data.drop(columns = ['thal'], axis = 1) # Null values is more than 50% of data, so, we delete the column.
data['slope']=data['slope'].fillna(value = data['slope'].mode()[0]) # Null values is  33% of data, so, we replace it with the mode value "flat".
data[data['oldpeak'] < 0] = data[data['oldpeak'] < 0] * -1 # oldpeak value has to be between 0:6.2, so we correct the values by multiply by -1.
data['oldpeak']=data['oldpeak'].fillna(value = data['oldpeak'].median()) # oldpeak null value we replaced it with the median value. 
data['exercise_induced_angina']= data['exercise_induced_angina'].fillna(value = data['exercise_induced_angina'].mode()[0])

 # These rows has "exercise_induced_angina" value = -1 so, we remove it.
row_indx_angina = data[data['exercise_induced_angina'] == -1].index
data = data.drop(index = row_indx_angina) 
# These rows has "max_heart_rate_achieved" value < 70 and negative values so, we remove it.
rows_indx_hr = data[(data['max_heart_rate_achieved']<70)].index
data = data.drop(index = rows_indx_hr)  
# print(data[(data['max_heart_rate_achieved']<70)].index)
# We replace the null values with the median value
data['max_heart_rate_achieved'] = data['max_heart_rate_achieved'].fillna(value = data['max_heart_rate_achieved'].median()) 
data['resting_electrocardiographic_results'] = data['resting_electrocardiographic_results'].fillna(value = data['resting_electrocardiographic_results'].mode()[0])
data['fasting_blood_sugar']= data['fasting_blood_sugar'].fillna(value = data['fasting_blood_sugar'].mode()[0])
# pressure values out of the range (90:200) not correct so, we remove it.
row_indx_bp = data[(data['resting_systolic_blood_pressure'] <90) ].index
data = data.drop(index =row_indx_bp) 
# We remove that row because the it out of the normal range (80:564)
row_indx_chol = data[data['cholesterol'] >564].index
data = data.drop(index = row_indx_chol) 
# Replaceing values which is equal (0) with the median value.
data['cholesterol'] = data['cholesterol'].replace(0, data['cholesterol'].median()) 
data['exercise_induced_angina'] = data['exercise_induced_angina'].astype('bool')
# print(data[(data['oldpeak'] <0) | (data['oldpeak'] >6.2)])

cleanData = data.to_csv(r'data\clean_data.csv')
print('complete')