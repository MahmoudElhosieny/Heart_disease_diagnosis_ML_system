from sklearn.pipeline import Pipeline
from pkgs.pipeLinePrepration import preprocessingObject
from pkgs.ML_functions import accuracy, F1_score, cross_accuracy
from pkgs.feature_target import x_train_new, x_test_new, y_train_new, y_test_new, x_new, y_new
from sklearn.ensemble import RandomForestClassifier


preprocessing = preprocessingObject()

RF_pipeline_model = Pipeline(steps = [
    ('preprocessing',preprocessing),
    ('model', RandomForestClassifier())
])

model = RF_pipeline_model
print('----Binary Classes for RF model------')
print('----Accuracy after Train-test-splite for RF model------')
accuracy(model,x_train_new, y_train_new, x_test_new, y_test_new)


print('---------F1-score for RF model -----------')
F1_score(model,x_test_new, y_test_new)  

print('---------Accuracy for RF model after Cross validation Technique --------')
cross_accuracy(model, x_new, y_new, 5)

print('done')