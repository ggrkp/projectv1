import csv
import sys
import sqlite3
import pandas as pd
import sklearn
import autosklearn
import autosklearn.metrics as mtc
fileName= "/home/larry/Documents/projectv1/Datasets/iris.csv"
df = pd.read_csv(fileName, sep="[,;]",
                 engine='python')
# print(df.head())
tar_idx = 4
target = df.iloc[:, (tar_idx)]
predictors = df.iloc[:, df.columns != df.columns[tar_idx]]
