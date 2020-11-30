# __________________________________________________________________________
# ----------------------- AUTOML & FEATURETOOLS IRIS.CSV -------------------
import numpy as np
import pandas as pd
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics
from sklearn.model_selection import train_test_split
import sklearn.metrics
import autosklearn.classification
from autosklearn.classification import AutoSklearnClassifier
import tsfresh
from tsfresh.feature_extraction import ComprehensiveFCParameters
from tsfresh.feature_extraction import extract_features
from tsfresh.utilities.dataframe_functions import impute
import datetime

# __________________________________________________________________________
#!----------------------- FILE LOAD ----------------------------------------
df = pd.read_csv("/home/ggeorg/Desktop/TSDataSets/sales.csv")
cnt = len(df.columns)
print(cnt)
header_list = []
for i in range(cnt):
    header_list.append(f"column {i}")
df.columns = header_list
df['Year'] = pd.DatetimeIndex(df['column 1']).year      # Xronia
# df['Month'] = pd.DatetimeIndex(df['Date']).month  # Mhnas
# df['Day'] = pd.DatetimeIndex(df['Date']).day  # Mera
# df["Week"] = pd.DatetimeIndex(df['Date']).weekofyear  # Mera

# df['Month_Year'] = pd.to_datetime(
#     df['Date']).dt.to_period('M')  # Mhnes ana xrono
 

# # df['Month_Year'] = pd.to_datetime(df['Date']).dt.to_period('M')
# df.head()

# # df.insert(0, 'id', range(len(df.index)))
# # df = df.drop(df.columns[[1]], axis=1)

# print(df.dtypes.astype(str).value_counts())
# print(df.head(30))

# # ? Ti simainei relevant features?  POIO EINAI TO Y?
# #! einai san feature selection ->
features = tsfresh.extract_features(
    df, column_id="Year")
final_features = impute(features)

print(final_features)

# #__________________________________________________________________________
# # #!----------------------- TARGET AND PREDICTORS ----------------------------
# tar_idx = 4
# y = df.iloc[:, (tar_idx)].to_numpy()  # Target Variable
# X = df.iloc[:, df.columns != df.columns[tar_idx]].to_numpy()  # Predictor Variables (All except the Target one.)              

# # #__________________________________________________________________________
# # #----------------------- SPLIT --------------------------------------------
# X_train, X_test, y_train, y_test = train_test_split( X, y, random_state=1 )
# # #__________________________________________________________________________
# # #!----------------------- AUTOSKLEARN CLASSIFIER ---------------------------
# automl = autosklearn.classification.AutoSklearnClassifier(
#     time_left_for_this_task=30,
#     per_run_time_limit=1,
#     tmp_folder='/tmp/autosklearn_resampling_example_tmp',
#     output_folder='/tmp/autosklearn_resampling_example_out',
#     disable_evaluator_output=False)
   
# # #__________________________________________________________________________
# # #!----------------------- FIT & FINAL ENSEBLE ------------------------------
# automl.fit(X_train, y_train, dataset_name = 'iris')
# # print(automl.show_models())
# predictions = automl.predict(X_test)
# # print(automl.sprint_statistics())
# print(automl.show_models())

# print("Accuracy score", sklearn.metrics.accuracy_score(y_test, predictions))
