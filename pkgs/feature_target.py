from pkgs.data import clean_data
from sklearn.model_selection import train_test_split



cleanData = clean_data
#Multi Classes data
x = cleanData[['age','sex','chest_pain','resting_systolic_blood_pressure','cholesterol','fasting_blood_sugar','resting_electrocardiographic_results','max_heart_rate_achieved','exercise_induced_angina','oldpeak','slope']]
y = cleanData[['num']]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)

#Binary Data
x_new = cleanData[['age','sex','chest_pain','resting_systolic_blood_pressure','cholesterol','fasting_blood_sugar','resting_electrocardiographic_results','max_heart_rate_achieved','exercise_induced_angina','oldpeak','slope']]
y_new = cleanData[['new_target']]

x_train_new, x_test_new, y_train_new, y_test_new = train_test_split(x_new, y_new, test_size = 0.2, random_state = 42)

print('done')