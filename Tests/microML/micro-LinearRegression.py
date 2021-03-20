import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from scipy.stats import loguniform
from micromlgen import port

from sklearn.model_selection import RepeatedStratifiedKFold


# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Use only one feature
diabetes_X = diabetes_X[:, np.newaxis, 2]

# Split the data into training/testing sets
X_train = diabetes_X[:-20]
X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
y_train = diabetes_y[:-20]
y_test = diabetes_y[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train,y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)

print('Mean squared error: %.2f'
      % mean_squared_error(y_test, y_pred))

print(port(regr))
# TODO: PREPEI NA ORISW SEARCH SPACE GIA NA KANW HP OPT !