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
from datetime import datetime
df = pd.read_csv("/home/ggeorg/Desktop/DataSets/iris.csv")
tar_idx = 4
y = df.iloc[:, (tar_idx)].to_numpy()  # Target Variable
X = df.iloc[:, df.columns != df.columns[tar_idx]].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

model = autosklearn.classification.AutoSklearnClassifier(
    time_left_for_this_task=30,
    per_run_time_limit=14,
    delete_output_folder_after_terminate=False,
    delete_tmp_folder_after_terminate=False,
    initial_configurations_via_metalearning=25
)

model = model.fit(X_train, y_train, dataset_name='pickled')

pickled_model = pickle.dumps(model)
#! INSERT
insertion_time = datetime.now()
conn = sqlite3.connect('modelsDB.db')
query = 'insert into models values (?, ?, ?)'
#todo: elegxos gia to an den dwthei name 
conn.execute(query, ["1", pickled_model, insertion_time])
conn.commit()
#!SELECT model
cursor = conn.execute('select * from models where name = "1"')
name, pickled_model, timestamp = cursor.fetchone()
fetched_model = pickle.loads(pickled_model)

print(fetched_model.show_models())