
# !22/12/2020 hofmann
import tsfresh
import pandas as pd
import numpy as np
#import tsfresh roll time series
from tsfresh.utilities.dataframe_functions import make_forecasting_frame
from tsfresh import extract_features    
from tsfresh import extract_relevant_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute

import autosklearn.regression
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics

df = pd.read_csv('births.csv', index_col=0, squeeze = True)
print (type(df))
# print(df)
# #insert id column for every row

# # df.insert(0, 'id', range(len(df.index)))
# # df.insert(0, 'id', 1    )

# #roll time series
df_shift , y = make_forecasting_frame(df, kind='sth', max_timeshift=15, rolling_direction=1)
print (type(df_shift))
print(type(y))
y.drop(y.tail(1).index,inplace=True) # drop last n rows

# print(y)
# print(df_shift)


X = extract_features(df_shift, column_id="time", column_value="value", n_jobs=0)
X = X.iloc[1:]

# print(X)
impute(X)
X_rl = select_features(X,y,show_warnings=False)
X=X_rl





X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=0)
automl = autosklearn.regression.AutoSklearnRegressor()
automl.fit(X_train, y_train)
y_hat = automl.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))

# # print(X)

# y = pd.read_csv('y_ftou', index_col=0, squeeze = True)

# X = extract_relevant_features(df_shift, y, column_id="time", column_sort="time", column_value="value", n_jobs=0)

# print(X)
