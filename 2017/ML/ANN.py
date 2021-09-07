import randomlist
import datetime
begin_time = datetime.datetime.now()
import csvReader
from copy import deepcopy
import pandas as pd
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier


#randomlist.nTest = 5
#randomlist.nSample = 10000 :: Training

training = []
traininglabels = []
for a in range(0,randomlist.nTest):
    t = []
    tl = []
    for j in range(0, randomlist.nSample):
        t.append(csvReader.data[randomlist.RList[a][j]])
        tl.append(csvReader.label[randomlist.RList[a][j]])
    training.append(t)
    traininglabels.append(tl)

test = []
testlabels = []
data = [deepcopy(csvReader.data) for i in range(randomlist.nTest)]
label = [deepcopy(csvReader.label) for i in range(randomlist.nTest)]

for i in range(0,randomlist.nTest):
    print(len(data[i]), i)
    for k in range(0, randomlist.nSample):

        data[i].pop(randomlist.RList[i][k] - k)
        label[i].pop(randomlist.RList[i][k] - k)
    test.append(data[i])
    testlabels.append(label[i])


for n in range(0,randomlist.nTest):
    min_max_scaler = preprocessing.MinMaxScaler()
    tra = min_max_scaler.fit_transform(training[n])
    clf = MLPClassifier(solver='lbfgs', alpha=1e-8,hidden_layer_sizes=(100, 30), random_state=1)
    clf.fit(tra, traininglabels[n])
    results = clf.predict(test[n])
    # print(results[0])
    # print(testlabels[n][0],"\n\n\n")

    counter = 0
    c = 0
    for m in range(0,len(results)):

        if(results[m] == testlabels[n][m]):
            counter = counter + 1
        if(testlabels[n][m] == 1):
            c = c+1

    counter2=0
    for k in range(0,len(tra)):
        if (traininglabels[n][k] == 1):
            counter2 = counter2 + 1

    print("Quant. de Ataques - Teste :",c)
    print("Quant. de Ataques - Training :",counter2)
    print("Quant. Ataques Total: ",c+counter2)
    print("Acertos: ",counter)
    print("Erros: ", len(results)-counter)
    print("Taxa de Acertos:", counter/len(results),"\n\n")

