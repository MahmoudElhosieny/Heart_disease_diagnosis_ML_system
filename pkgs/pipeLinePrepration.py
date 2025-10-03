from sklearn.pipeline import Pipeline
from pkgs.feature_target import x, y
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


features = x
target = y

#numerical features
numerical_features = features.select_dtypes(include=['int64','float64']).columns.tolist()

# categorical_features
categorical_features = features.select_dtypes(include = ['object','bool','category']).columns.tolist()

# Preprocessing Pipeline
numerical_pipeline = Pipeline(steps = [('scaling',StandardScaler())])
categorical_pipeline = Pipeline(steps = [('encoding', OneHotEncoder(handle_unknown = 'ignore'))])

preprocessing = ColumnTransformer(transformers = [
    ('numerical_preprocessing', numerical_pipeline, numerical_features),
    ('categorical_preprocessing', categorical_pipeline, categorical_features)
])

def preprocessingObject():
    return preprocessing

print('Done')


