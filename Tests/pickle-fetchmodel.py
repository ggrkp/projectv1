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
cursor = conn.execute('select * from models where name = "model2"')
name, pickled_model = cursor.fetchone()
print(name)
fetched_model = pickle.loads(pickled_model)

print(fetched_model.show_models())