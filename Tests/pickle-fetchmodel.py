# this is a test file for pickling and loading data on sqlite
#! pickle implementation -> reuse models

import numpy as np
import pandas as pd
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics
from sklearn.model_selection import train_test_split
import sklearn.metrics
import autosklearn.classification
from autosklearn.classification import AutoSklearnClassifier
import pickle
import sqlite3
#! connect to database
conn = sqlite3.connect('modelsDB.db')
#!SELECT model
model_name = 'model2' 
cursor = conn.execute(f'select * from models where name = "{model_name}"')
name, pickled_model, ttimestamp = cursor.fetchone()
print(name,ttimestamp)
fetched_model = pickle.loads(pickled_model)

print(fetched_model.show_models())

df = pd.read_csv("/home/ggeorg/Desktop/DataSets/iris.csv")

tar_idx = 4

X = df.iloc[:, df.columns != df.columns[tar_idx]].to_numpy()
y = df.iloc[:, (tar_idx)].to_numpy()  # Target Variable

score = fetched_model.score(X, y)

print("Test Score with pickle model: {0:.2f} %". format(100 * score))

y_predict = fetched_model.predict(X)

print(y_predict)