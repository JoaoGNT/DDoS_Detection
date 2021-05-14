import datetime
begin_time = datetime.datetime.now()
import csvReader
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
import random


training = []
trainingLabels= []

randomlist = sorted(random.sample(range(0, len(csvReader.data)), 10000))


for j in range(0,len(randomlist)):
    training.append(csvReader.data[randomlist[j]])
    trainingLabels.append(csvReader.label[randomlist[j]])

for k in range(0, len(randomlist)):
    csvReader.data.pop(randomlist[k]-k)
    csvReader.label.pop(randomlist[k]-k)

test = csvReader.data
testlabel = csvReader.label

min_max_scaler = preprocessing.MinMaxScaler()
training = min_max_scaler.fit_transform(training)


clf = MLPClassifier(solver='lbfgs', alpha=1e-8,hidden_layer_sizes=(20, 5), random_state=1)
clf.fit(training, trainingLabels)
results = clf.predict_proba(test)

# print(len(results))
# print(len(testlabel),"\n\n\n")
# print(results)

print(results[0][0])
print(testlabel[0],"\n\n\n")

counter = 0
c=0
for m in range(0,len(results)):

    if(results[m][0] == testlabel[m]):
        counter = counter + 1
    if(testlabel == 1):
        c = c+1

print("Quant. de Ataques - Teste :",c)

print("Acertos: ",counter)
print("Erros: ", len(results)-counter)
print("Taxa de Acertos:", counter/len(results))




# print(data[0])
# ModelAnn = MLPClassifier()
# parameters = {'solver': ['adam'], 'alpha': [1e-5, 1e-3, 1e-1],
#               'hidden_layer_sizes': [(25, 50, 10), (50, 50, 10), (100, 100, 10), (100, 50, 10), (50, 10)],
#               'random_state': [1], 'activation': ['identity', 'relu', 'logistic']}
# clf = GridSearchCV(ModelAnn, parameters, cv=10)
# clf.fit(data, csvReader.label)
#
# dataFrame = pd.DataFrame.from_dict(clf.cv_results_)
# dataFrame.to_excel("annEDistance.xlsx", sheet_name="ann")
# print(clf.best_params_)
#
# print('Time Elapsed(s):',datetime.datetime.now() - begin_time)


