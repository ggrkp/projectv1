from micromlgen import port
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn import metrics


cancer = load_breast_cancer()

# The data set is presented in a dictionary form:
print(cancer.keys())
df_feat = pd.DataFrame(cancer['data'],
                       columns=cancer['feature_names'])

# cancer column is our target
df_target = pd.DataFrame(cancer['target'],
                         columns=['Cancer'])


X_train, X_test, y_train, y_test = train_test_split(
    df_feat, np.ravel(df_target),
    test_size=0.30, random_state=101)

regressor = RandomForestClassifier()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print('ACC : ', metrics.accuracy_score(y_test, y_pred))

# ? Apotelesmata xwris hptuning
# !Mean Absolute Error: 0.07978070175438595
# !Mean Squared Error: 0.0363718201754386
# !Root Mean Squared Error: 0.19071397477751492

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
rf_random = RandomizedSearchCV(regressor, param_distributions=random_grid,
                               n_iter=100, cv=3, verbose=2, random_state=42, n_jobs=-1)

rf_random.fit(X_train, y_train)
rf_random.best_params_
y_pred = rf_random.best_estimator_.predict(X_test)

print (rf_random.best_estimator_)
print('ACC : ', metrics.accuracy_score(y_test, y_pred))
# print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
# print('Root Mean Squared Error:', np.sqrt(
#     metrics.mean_squared_error(y_test, y_pred)))

# ? apotelesmata meta apo to hp tuning
#! Mean Absolute Error: 0.08362573099415205
#! Mean Squared Error: 0.05207602339181287
#! Root Mean Squared Error: 0.22820171645238094

print(port(rf_random.best_estimator_))

