from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from pkgs.pipeLinePrepration import preprocessingObject
from pkgs.ML_functions import accuracy, F1_score, cross_accuracy
from pkgs.feature_target import x_train, x_test, y_train, y_test, x, y



preprocessing = preprocessingObject()

LR_pipeline_model = Pipeline(steps = [
    ('preprocessing',preprocessing),
    ('model', LogisticRegression())
])

model = LR_pipeline_model
print('----Accuracy after Train-test-splite for LR model------')
accuracy(model,x_train, y_train, x_test, y_test)


print('---------F1-score for LR model -----------')
F1_score(model,x_test, y_test)  

print('---------Accuracy for LR model after Cross validation Technique --------')
cross_accuracy(model, x, y, 5)

print('done')