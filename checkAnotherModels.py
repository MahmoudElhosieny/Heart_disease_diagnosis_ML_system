from pkgs.ML_functions import accuarcy_comparison
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from pkgs.pipeLinePrepration import preprocessingObject
from sklearn.pipeline import Pipeline
from pkgs.ML_functions import accuarcy_comparison
from pkgs.feature_target import x_new, y_new

preprocessing =preprocessingObject()
# models pipeline
DT_pipeline_model = Pipeline(steps = [
    ('preprocessing',preprocessing),
    ('model', DecisionTreeClassifier(criterion = 'entropy'))
])

KNN_pipeline_model = Pipeline(steps = [
    ('preprocessing',preprocessing),
    ('model', KNeighborsClassifier())
])

SVM_pipeline_model = Pipeline(steps = [
    ('preprocessing',preprocessing),
    ('model', SVC(kernel = 'rbf')) # 'rbf':Radial Basis Function is the most popular and versatile kernel available
])

models = [DT_pipeline_model, KNN_pipeline_model, SVM_pipeline_model]

# Check another models
accuarcy_comparison(models, x_new, y_new, 9)
print('Done')

