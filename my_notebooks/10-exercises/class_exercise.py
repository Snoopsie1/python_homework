# TODO: 1) Use these imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import auc, roc_curve, confusion_matrix
# TODO: 2) Get the data into a pandas dataframe
data = pd.read_csv("../../data/AB_NYC_2019.csv", sep=",")
print(data)
# TODO: 3) Add a column to the dataframe: “is_cheap”,
#  that contains boolean values for the price being below median.
#  Hint: DataFrame has a median() method. This column contains our target data: y

data["isCheap"] = data.price < data.price.median()
print(data)