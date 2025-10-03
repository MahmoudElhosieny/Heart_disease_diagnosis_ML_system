from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import cross_val_score





# Classification Report function
def ClassificationReport(model, x_test, y_test, model_name):
    predicted_y = model.predict(x_test)
    report = classification_report(y_test, predicted_y,zero_division=0)
    print(f'-------{model_name} -- Classification Report --------')
    print(report)

# Accuracy by Train test splite technique
def accuracy(model, x_train, y_train, x_test, y_test):
    model.fit(x_train, y_train.values.ravel())
    print(f'Accuracy of training data {round(model.score(x_train, y_train)*100,2)}%')
    print(f'Accuracy of test data {round(model.score(x_test, y_test)*100,2)} %')

# F1-score function
def F1_score(model, x_test, y_test):
    predicted_y = model.predict(x_test)
    f1_score_micro = f1_score(y_test, predicted_y, average = 'micro')
    f1_score_macro = f1_score(y_test, predicted_y, average = 'macro')
    print('------ F1-Score Result --------')
    print(f'f1_score_micro :{round(f1_score_micro*100, 2)} %') # type: ignore
    print(f'f1_score_macro :{round(f1_score_macro*100, 2)} %') # type: ignore

# Accuracy by Cross validation technique
def cross_accuracy(model, x, y, cv):
    score = cross_val_score(model, x, y.values.ravel(), cv = cv)
    mean_score = score.mean()
    print('------ Accuracy after using Cross val score function -------')
    print(f'Mean accuracy value: {round(mean_score*100,2)}%')

# Check another Models
def accuarcy_comparison(models, x, y, cv):
    for index, model in enumerate(models):
        score = cross_val_score(model, x, y.values.ravel(), cv = cv)
        accuracy = round(score.mean()*100,2)
        if index == 0:
            print(f'Accuracy of DT_model: {accuracy} %')
        elif index == 1:
             print(f'Accuracy of KNN_model: {accuracy} %')
        else: 
             print(f'Accuracy of SVM_model: {accuracy} %')


print('done')