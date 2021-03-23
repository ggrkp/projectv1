import pandas as pd 
import numpy as np 
from micromlgen import port
from sklearn.metrics import classification_report, confusion_matrix 
from sklearn.datasets import load_breast_cancer 
from sklearn.svm import SVC 
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
# import pylab as pl
from sklearn import datasets 

  
iris = datasets.load_iris()
df_feat = iris.data# we only take the first two features. 
df_target = iris.target
  
# The data set is presented in a dictionary form: 

  
print("Feature Variables: ") 
# print(df_feat.info()) 
print("Dataframe looks like : ") 
# print(df_feat.head()) 
from sklearn.model_selection import train_test_split 
  
X_train, X_test, y_train, y_test = train_test_split( 
                        df_feat, np.ravel(df_target), 
                test_size = 0.30, random_state = 101) 

# train the model on train set 
model = SVC() 
model.fit(X_train, y_train) 
  
# print prediction results 
predictions = model.predict(X_test) 
print(classification_report(y_test, predictions)) 


# defining parameter range 
param_grid = {'C': [0.1, 1, 10, 100, 1000],  
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001], 
              'kernel': ['rbf']}  
  
grid = RandomizedSearchCV(SVC(), param_grid, refit = True, verbose = 3) 
  
# fitting the model for grid search 
grid.fit(X_train, y_train) 


# print best parameter after tuning 
print(grid.best_params_) 
  
# print how our model looks after hyper-parameter tuning 
print(grid.best_estimator_) 

grid_predictions = grid.best_estimator_.predict(X_test) 
  
# print classification report 
print(classification_report(y_test, grid_predictions)) 

print(port(grid.best_estimator_))


 