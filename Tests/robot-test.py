

#! Gemizw me headers an den uparxoun:
# todo Na to ftiaksw se function gia to app mou!
# cnt = len(df.columns)
# header_list = []
# for i in range(cnt):
#     header_list.append(f"column{i}")
# df.columns = header_list

#! extract info drom time/date columns:
# df['ID'] = pd.DatetimeIndex(df[ts_col]).date  # Mhnas
# print(df.shape)
# df = df.drop(ts_col, axis=1)
# df = df.drop('id',axis=1)
# df = df.reset_index()
# # df['Day'] = pd.DatetimeIndex(df['Date']).day  # Mera
# # df["Week"] = pd.DatetimeIndex(df['Date']).weekofyear  # Mera
# print(df.head(20))

#! Genikes paratiriseis:
# * to ts_col tha dinetai apo to xristi opws akrivws dinetai kai to target feature sto antistoixo screen
# * kai meta tha kserei to sustima oti tha prepei na tokanei drop gia na mhn trwei error
# * isws na petaei to neo df se kainourio temp file kai sto telos tou
# * session na to diagrafei h na ftiaxnei diafora temp files me diaforetikes epiloges apo to xristi kai sto telos na kanei ta panta clear
# * settings giati ama valw default crasharei
# * ta settings mporoun na dinontai kai auta apo to xristi px na dinontai kapoies vasikes epiloges gia ti dimiourgia features sto
# * ts fresh kai na mhn ftiaxnontai 800 diaforetika default features. Mporw na ftiaksw ena default dictionary to opoio na trexei kai na ftiaxnei
# * enan apodekto arithmo apo features xwris na krasarei o dias h toulaxiston na petaei WARNING: THA PETHANETE APO ELLEIPSH RAM
# * prepei  kapws na anagnwrizw ti epiloges uparxoun gia extraction dld an exei date kai time analutika h mono month h mono date ktl

# todo: na dialeksw polla diaforetika datasets timeseries
# todo : genika prepei na oristei ena epitrepto format sto file pou ginetai import.
#! sunspots , occ1 , occ2 , occ3 , ozone , ozone1
# todo : create new features-> new data set for classification and regression

import tsfresh as ts
import pandas as pd
import numpy as np
from pandas import read_csv
from sklearn.model_selection import train_test_split
import matplotlib
from matplotlib import pyplot as plt
import tsfresh
from tsfresh.feature_extraction import ComprehensiveFCParameters
from tsfresh.feature_extraction import extract_features
import datetime
from tsfresh.utilities.dataframe_functions import add_sub_time_series_index
from tsfresh.examples import load_robot_execution_failures

# example from tsfresh
# data, y = load_robot_execution_failures()
# print(f"ROBOT  DATASET : {data}")
# print(f"TARGET DATASET : {y}")

path = "/home/ggeorg/Desktop/TSDataSets/Robots/"
# path = "/home/ggeorg/Desktop/TSDataSets/"
target_csv = "y_train.csv"
features_csv = "X_train.csv"
data = pd.read_csv(path+features_csv)
y = pd.read_csv(path+target_csv, header=0, parse_dates=[0], squeeze=True, index_col=0)
print(type(y))
# entities = (len(df.index)/6)  # ! set number of entities (e.g. Robots)
# # ! split Data into subseries depending on number of entities
# add_sub_time_series_index(df, int(entities))

print(data)
print(y)

# prepei na kanw extract to date col

ts_col = 'row_id'
col_id = 'series_id'
# settings = {"mean": None,"variation_coefficient":None}

relevant_features = tsfresh.extract_relevant_features(
    data, y, column_id=col_id, column_sort=ts_col, column_value="linear_acceleration_Y")

just_features = tsfresh.extract_features(
    data, column_id=col_id, column_sort=ts_col,column_value="linear_acceleration_Y")

print(just_features)
print(relevant_features)
# print(features)
# features.plot()
# plt.show()
# features.to_csv("feat.csv")
