from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from pkgs.pipeLinePrepration import preprocessingObject
from pkgs.ML_functions import accuracy, F1_score, cross_accuracy
from pkgs.feature_target import x_train_new, x_test_new, y_train_new, y_test_new, x_new, y_new
from sklearn.model_selection import  GridSearchCV
import pickle



preprocessing = preprocessingObject()

LR_pipeline_model = Pipeline(steps = [
    ('preprocessing',preprocessing),
    ('model', LogisticRegression(max_iter=1500, solver="saga"))
])

model = LR_pipeline_model
print('----Binary Classes for LR model------')
print('----Accuracy after Train-test-splite for LR model------')
accuracy(model,x_train_new, y_train_new, x_test_new, y_test_new)


print('---------F1-score for LR model -----------')
F1_score(model,x_test_new, y_test_new)  

print('---------Accuracy for LR model after Cross validation Technique --------')
cross_accuracy(model, x_new, y_new, 5)


print('--------------------Hypertuning for LR model----------')
param_grid = {
    'model__penalty':['l2','l1'], #l1: lasso & l2: Ridge the type of regularization applied
    'model__C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], #The Regularization Strength (C)
    'preprocessing__numerical_preprocessing__scaling__with_mean': [True, False]
}
grid_model = GridSearchCV(estimator = model, param_grid = param_grid, scoring = 'f1', cv = 6)
grid_model.fit(x_train_new, y_train_new.values.ravel())

print('-------------- F1-Score --------')
print(f'The highest mean f1-score for LogisticRegression Model: {round(grid_model.best_score_ *100,2)} %')

# Saving model
best_model = grid_model.best_estimator_
with open(r'models\best_model_LR.pkl', 'wb') as file:
    pickle.dump(best_model,file)
print('done')

