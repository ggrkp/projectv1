import tsfresh
import pandas as pd
import numpy as np
from tsfresh.utilities.dataframe_functions import roll_time_series
from tsfresh import extract_features
from tsfresh import extract_relevant_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute
from pandas import Series
from numpy.random import randn

import sklearn.datasets
import sklearn.metrics
import autosklearn.classification


if __name__ == '__main__':

    df = pd.read_csv('/home/larry/Documents/projectv1/Datasets/occupancy.csv')
    df.insert(0, 'id', 0)
    print(df.head())
    print ('................................................ok................................................')
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------------------------------------------------')

    df_rolled = roll_time_series(
        df, column_id="id", column_sort="date", min_timeshift=0, rolling_direction=1)
    print("\nTHE ROLLED TIME SERIES DATAFRAME IS:\n", df_rolled)
    print ('................................................ok................................................')
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------------------------------------------------')

    y = df.iloc[:, 7].values
    y = pd.Series(y)
    print(type(y))

    print("Target Variable: \n", y)
    print ('................................................ok................................................')
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    X = extract_features(
        df_rolled, column_id='id', column_sort='date')
    X.reset_index(drop=True, inplace=True)
    impute(X)
    X = select_features(X,y,show_warnings=False)

    print ('................................................ok................................................')

    print("Extracted features (Relevant):\n", X)
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------------------------------------------------')

    print("---------------AUTOML STARTING NOW!-------------------")

    ############################################################################
    # Data Loading
    # ============
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X, y, random_state=1)

    ############################################################################
    # Build and fit a regressor
    # =========================

    automl = autosklearn.classification.AutoSklearnClassifier(
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
    print("Accuracy score:", sklearn.metrics.accuracy_score(y_test, predictions))
    print(predictions)
    print(y_test)
    
    print("---------------AUTOML DONE!-------------------")

    
    
    
    
    
    
    