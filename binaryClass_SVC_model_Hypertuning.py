from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from pkgs.pipeLinePrepration import preprocessingObject
from pkgs.ML_functions import accuracy, F1_score, cross_accuracy
from pkgs.feature_target import x_train_new, x_test_new, y_train_new, y_test_new, x_new, y_new
from sklearn.model_selection import  GridSearchCV
import pickle



preprocessing = preprocessingObject()

SVM_pipeline_model = Pipeline(steps = [
    ('preprocessing',preprocessing),
    ('model', SVC(kernel = 'rbf')) # 'rbf':Radial Basis Function is the most popular and versatile kernel available
])

model = SVM_pipeline_model
print('----Binary Classes for SVC model------')
print('----Accuracy after Train-test-splite for SVC model------')
accuracy(model,x_train_new, y_train_new, x_test_new, y_test_new)


print('---------F1-score for SVC model -----------')
F1_score(model,x_test_new, y_test_new)  

print('---------Accuracy for SVC model after Cross validation Technique --------')
cross_accuracy(model, x_new, y_new, 5)


print('--------------------Hypertuning for SVC model----------')
param_grid = {
    'model__gamma':[0.001, 0.01, 0.1, 1], 
    'model__C': [0.1, 1, 10, 100],
    'preprocessing__numerical_preprocessing__scaling__with_mean': [True, False]}

grid_model = GridSearchCV(estimator = model, param_grid = param_grid, scoring = 'f1', cv = 6)
grid_model.fit(x_train_new, y_train_new.values.ravel())

print('-------------- F1-Score --------')
print(f'The highest mean f1-score for Support Vector Classifier Model: {round(grid_model.best_score_ *100,2)} %')

# Sving Model 
SVC_model = grid_model.best_estimator_
with open(r'models\best_model_SVC.pkl', 'wb') as file:
    pickle.dump(SVC_model,file)
print('done')