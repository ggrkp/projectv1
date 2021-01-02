import tsfresh
import pandas as pd
import numpy as np
from tsfresh.utilities.dataframe_functions import roll_time_series  
from tsfresh import extract_features    
from tsfresh import extract_relevant_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute
import sklearn.datasets
import sklearn.metrics
import autosklearn.regression



if __name__ == '__main__':

    df = pd.read_csv('/home/larry/Documents/projectv1/Datasets/occupancy.csv')
    df.insert(0, 'id', 0)
    print(df.head())
    df_rolled = roll_time_series(df, column_id="id", column_sort="date", min_timeshift=0, rolling_direction=1)
    print ("\nTHE ROLLED TIME SERIES DATAFRAME IS :\n",df_rolled.head())
    

    X = extract_features(df_rolled, column_id='id', column_sort='date')
    # X = X.iloc[1:]
    print(X)