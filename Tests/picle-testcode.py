# this is a test file 
# pickle implementation -> reuse models
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

# df = pd.read_csv("/home/ggeorg/Desktop/DataSets/iris.csv")
# tar_idx = 4
# y = df.iloc[:, (tar_idx)].to_numpy()  # Target Variable
# X = df.iloc[:, df.columns != df.columns[tar_idx]].to_numpy()
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# model = autosklearn.classification.AutoSklearnClassifier(
#     time_left_for_this_task=30,
#     per_run_time_limit=14,
#     delete_output_folder_after_terminate=False,
#     delete_tmp_folder_after_terminate=False
# )

# model = model.fit(X_train, y_train, dataset_name='pickled')

# pickle name
pkl_filename = "pickle_model.pkl"
# with open(pkl_filename, 'wb') as file:
#     pickle.dump(model, file)

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

# pickle_model.fit(X_train, y_train, dataset_name='iris')

# print(pickle_model.show_models())
# score = pickle_model.score(X_test, y_test)

# print("Test Score with pickle model: {0:.2f} %". format(100 * score))

# y_predict = pickle_model.predict(X_test)

print(pickle_model.show_models())
