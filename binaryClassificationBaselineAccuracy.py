from pkgs.data import clean_data
from sklearn.metrics import accuracy_score
from pkgs.ML_functions import ClassificationReport
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.dummy import DummyClassifier
from pkgs.feature_target import x_new, y_new, x_train_new, x_test_new, y_train_new, y_test_new 
cleanData = clean_data

x = x_new
y = y_new

# Train test split data
x_train_new, x_test_new, y_train_new, y_test_new = train_test_split(x,y,test_size = 0.2, random_state = 42)
dummy_model = DummyClassifier(strategy = 'most_frequent', random_state = 42)
dummy_model.fit(x_train_new, y_train_new)

dummy_pred_y = dummy_model.predict(x_test_new)
dummy_accuracy = accuracy_score(y_test_new, dummy_pred_y)
# Baseline accuracy train_test_splite technique 
print('-------------Binary Classification--------------')
print('Baseline accuracy train_test_splite technique')
print(f'The dummy model accuracy: {round(dummy_accuracy * 100,2)} %') 

print('------------------------------------------')
#Cross validation technique
score_accuarcy = cross_val_score(dummy_model, x,y, cv = 8, scoring = 'accuracy')
meanScore = score_accuarcy.mean()
print('Baseline accuracy Cross validation technique')
print(f'The dummy model accuracy: {round(meanScore * 100,2)} %')
print('------------------------------------------')
ClassificationReport(dummy_model, x_test_new, y_test_new, 'Dummy model') 
print('Done')