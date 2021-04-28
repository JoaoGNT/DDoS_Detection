import datetime
begin_time = datetime.datetime.now()
import pandas as pd
from sklearn import preprocessing
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import csvReader

min_max_scaler = preprocessing.MinMaxScaler()
data = min_max_scaler.fit_transform(csvReader.data)
ModelSvm = svm.SVC()

parameters = {'kernel': ('linear', 'rbf', 'poly'), 'C': [10 ** -4, 1, 10 ** 4], 'degree': [2, 5],
              'gamma': [10 ** -(1 / 2), 1, 10 ** (1 / 2)], 'random_state': [1]}

clf = GridSearchCV(ModelSvm, parameters, cv=10)
clf.fit(data, csvReader.label)
print('a')
dataFrame = pd.DataFrame.from_dict(clf.cv_results_)
dataFrame.to_excel("svm.xlsx", sheet_name="svm")
print(clf.best_params_)

print('Time Elapsed(s):',datetime.datetime.now() - begin_time)