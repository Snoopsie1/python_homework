import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data', sep=",", header=None)
data = pd.read_csv('balance-scale.data', sep=',', header=None)
print(f"Dataset Length: {len(data)}")
print(f"Dataset Shape: {data.shape}")
# TODO: 3 Split Dataset (input variables and target) Hint: first column is the target
X = data.values[:, 1:5]
Y = data.values[:, 0]
# TODO: 4 Split dataset into training data and test data using train_test_split()
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size= 0.3, random_state = 100)
# TODO: 5 Create a model (DecisionTreeClassifier(criterion = “gini”, random_state=100,max_depth=3, min_samples_leaf=5)
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth = 3, min_samples_leaf = 5)
# TODO: 6 Fit model with training data
clf_gini.fit(X_train, y_train)
# TODO: 7 Make predictions on test data (using predicted_y = prediction(X_test, model))
y_pred = clf_gini.predict(X_test)
# TODO: 8 Calculate model accuracy with cal_accuracy(y_test, predicted_y)
print(f"Accuracy : {accuracy_score(y_test, y_pred)*100}")
