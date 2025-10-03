from sklearn.metrics import accuracy_score
from pkgs.ML_functions import ClassificationReport
from sklearn.model_selection import cross_val_score
from sklearn.dummy import DummyClassifier
from pkgs.feature_target import x, y, x_train, x_test, y_train, y_test 

x = x
y = y

# Train test split data
dummy_model = DummyClassifier(strategy = 'most_frequent', random_state = 42)
dummy_model.fit(x_train, y_train)

dummy_pred_y = dummy_model.predict(x_test)
dummy_accuracy = accuracy_score(y_test, dummy_pred_y)
# Baseline accuracy train_test_splite technique 
print('---------Multi classification ----------')
print('Baseline accuracy train_test_splite technique')
print(f'The dummy model accuracy: {round(dummy_accuracy * 100,2)} %') 

print('------------------------------------------')
#Cross validation technique
score_accuarcy = cross_val_score(dummy_model, x,y, cv = 8, scoring = 'accuracy')
meanScore = score_accuarcy.mean()
print('Baseline accuracy Cross validation technique')
print(f'The dummy model accuracy: {round(meanScore * 100,2)} %')
print('------------------------------------------')
ClassificationReport(dummy_model, x_test, y_test, 'Dummy model') 
