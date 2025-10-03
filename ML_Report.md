# Conclusion:

# (1)- Multi-class classification using LogisticRegression & RandomForestClassifier is very poor with an accuracy of 50% with that data, so we will make the problem a binary classification.

# (2)- Baseline accuracy is 55%.

# (3)- By using Train-test split technique with test-size =0.2, we get that:

(a)- Accuracy score and f1-score are the same, 76.8% from the RF-model and 77.9% from the LR-model.

# (4)- By using the cross-validation technique to train and test the model, we get that:

(a)- Max. accuracy from the LogisticRegression model is 78.25% at cv = 5.
(b)- Max. accuracy from the RandomForestClassifier model is 77.6% at cv =9.

# (5)- By checking another model:

(a)- We get max. Accuracy is 78.69% from the SVM model at cv = 9 by using the cross-validation technique.

# (6)- From all notes, we get that:

(a)- The LogisticRegression Model accuracy of 78.25%.
(b)- The SVM model accuracy of 78.69%.
(c)- We can use LogisticRegression or SVM model for our program.
(d)- The program will be a binary classification to predict if the patient is healthy (class 0) or sick (class 1).

# (7)- After Hyperparameter Tuning using GridSearchCV for LogisticRegression model, we get that:

(a)- The highest mean accuracy for LogisticRegression Model: 80.42 % at cv = 6.
(b)- The highest mean f1-score for LogisticRegression Model: 82.16 % at cv = 6.

# (8)- After Hyperparameter Tuning using GridSearchCV for SVC model, we get that:

(a)- The highest mean f1-score for SVC Model: 83.81 % at cv = 10.
(b)- The highest mean accuracy for SVC Model: 81.81 % at cv = 7.

# (9)- The data is imbalanced, so we will depend on the F1-score, which is:

(a)- 82.16 % at cv = 6, for LogisticRegression, and I think it is acceptable for our program.
(b)- 83.81 % at cv = 10, for SVC model, and I think it is acceptable for our program also.
