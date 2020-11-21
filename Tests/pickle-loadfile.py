# this is a test file for pickling and storing data on sqlite
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

pkl_filename = "pickle_model.pkl"

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

print(pickle_model.show_models())


print(pickle_model.show_models())
