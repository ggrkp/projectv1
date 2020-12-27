
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


import sklearn.datasets
import sklearn.metrics

import autosklearn.regression

if __name__ == '__main__':

    df = pd.read_csv('/home/larry/Documents/projectv1/Datasets/shampoo.csv', index_col=0, squeeze = True)
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
    X = select_features(X,y,show_warnings=False)

    print ('ok')
    print(X)



    ############################################################################
    # Data Loading
    # ============
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=1)

    ############################################################################
    # Build and fit a regressor
    # =========================

    automl = autosklearn.regression.AutoSklearnRegressor(
        time_left_for_this_task=30,
        per_run_time_limit=14,
    )
    automl.fit(X_train, y_train, dataset_name='ts')

    ############################################################################
    # Print the final ensemble constructed by auto-sklearn
    # ====================================================

    print(automl.show_models())

    ###########################################################################
    # Get the Score of the final ensemble
    # ===================================

    predictions = automl.predict(X_test)
    print("R2 score:", sklearn.metrics.r2_score(y_test, predictions))
    print('MAX ERROR',sklearn.metrics.max_error(y_test, predictions) )
    print(predictions)
    print(y_test)
    # # print(X)

    # y = pd.read_csv('y_ftou', index_col=0, squeeze = True)

    # X = extract_relevant_features(df_shift, y, column_id="time", column_sort="time", column_value="value", n_jobs=0)

    # print(X)
