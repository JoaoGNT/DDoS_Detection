import datetime
begin_time = datetime.datetime.now()
import csvReader
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier


min_max_scaler = preprocessing.MinMaxScaler()
data = min_max_scaler.fit_transform(csvReader.data)
print(data[0])
ModelAnn = MLPClassifier()
parameters = {'solver': ['adam'], 'alpha': [1e-5, 1e-3, 1e-1],
              'hidden_layer_sizes': [(25, 50, 10), (50, 50, 10), (100, 100, 10), (100, 50, 10), (50, 10)],
              'random_state': [1], 'activation': ['identity', 'relu', 'logistic']}
clf = GridSearchCV(ModelAnn, parameters, cv=10)
clf.fit(data, csvReader.label)

dataFrame = pd.DataFrame.from_dict(clf.cv_results_)
dataFrame.to_excel("annEDistance.xlsx", sheet_name="ann")
print(clf.best_params_)

print('Time Elapsed(s):',datetime.datetime.now() - begin_time)