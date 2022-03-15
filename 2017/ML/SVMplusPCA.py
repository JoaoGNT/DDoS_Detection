import randomlist
from datetime import datetime
import csvReader
from copy import deepcopy
from sklearn import preprocessing
from sklearn import svm
from sklearn.decomposition import PCA


begining_process = datetime.now()
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
    #print(len(data[i]), i)
    for k in range(0, randomlist.nSample):

        data[i].pop(randomlist.RList[i][k] - k)
        label[i].pop(randomlist.RList[i][k] - k)
    test.append(data[i])
    testlabels.append(label[i])

end_processtime = datetime.now()
time2process = end_processtime - begining_process

C = [0.001 , 1 , 1000]
degree = [2,3,4]
gamma = [10 ** (-1), 1, 10 ** (2)]
#components = 70
components = [49, 35, 21]
'''
## ------------ LINEAR
print('LINEAR')

for n in range(0,randomlist.nTest):
    print('Test:', n)

    min_max_scaler = preprocessing.MinMaxScaler()
    tra = min_max_scaler.fit_transform(training[n])
    tst = min_max_scaler.fit_transform(test[n])
    for c in range(0, len(components)):
        begining_transform = datetime.now()
        print('n_components:',components[c])
        pca=PCA(n_components=components[c])
        pca.fit(tra)
        tra = pca.transform(tra)
        tst = pca.transform(tst)
        end_transform = datetime.now()
        for l in range(0,len(C)):
            begining_training = datetime.now()
            clf = svm.SVC(C=C[l],kernel='linear',random_state=1,class_weight={0:1,1:3})
            clf.fit(tra, traininglabels[n])
            results = clf.predict(tst)
            end_training = datetime.now()

            counter = 0
            c = 0
            verd_positivo = 0
            verd_negativo = 0
            falso_positivo = 0
            falso_negativo = 0
            erros = 0

            for m in range(0, len(results)):

                if (results[m] == testlabels[n][m]):
                    counter = counter + 1
                    if (results[m] == 1):
                        verd_positivo = verd_positivo + 1
                    if (results[m] == 0):
                        verd_negativo = verd_negativo + 1

                if (results[m] != testlabels[n][m]):
                    erros = erros + 1
                    if (results[m] == 1):
                        falso_positivo = falso_positivo + 1
                    if (results[m] == 0):
                        falso_negativo = falso_negativo + 1

                if (testlabels[n][m] == 1):
                    c = c + 1

            counter2 = 0
            for r in range(0, len(tra)):
                if (traininglabels[n][r] == 1):
                    counter2 = counter2 + 1

            time2training = end_training - begining_training
            time2tranform = end_transform - begining_transform
            print('Time Elapsed(s):', (time2process + time2training + time2tranform))
            print('C:', C[l])
            print("Quant. de Ataques - Teste :", c)
            print("Quant. de Ataques - Training :", counter2)
            print("Quant. Ataques Total: ", c + counter2)
            print("Acertos: ", counter)
            print("Verd-Pos: ", verd_positivo)
            print("Verd-Neg: ", verd_negativo)
            print("Erros: ", len(results) - counter)
            print("Falso-Pos: ", falso_positivo)
            print("Falso-Neg: ", falso_negativo)
            print("Taxa de Acertos:", counter / len(results), "\n\n")

### --- End Linear

    ## ------------ RBF
print('RBF')
for n in range(0,randomlist.nTest):
    print('Test:', n)

    min_max_scaler = preprocessing.MinMaxScaler()
    tra = min_max_scaler.fit_transform(training[n])
    tst = min_max_scaler.fit_transform(test[n])
    for c in range(0, len(components)):
        begining_transform = datetime.now()
        print('n_components:',components[c])
        pca=PCA(n_components=components[c])
        pca.fit(tra)
        tra = pca.transform(tra)
        tst = pca.transform(tst)
        end_transform = datetime.now()
        for l in range(0,len(C)):
            for g in range(0,len(gamma)):
                begining_training = datetime.now()
                clf = svm.SVC(C=C[l],kernel='rbf',random_state=1,class_weight={0:1,1:3},gamma=gamma[g])
                clf.fit(tra, traininglabels[n])
                results = clf.predict(tst)
                end_training = datetime.now()

                counter = 0
                c = 0
                verd_positivo = 0
                verd_negativo = 0
                falso_positivo = 0
                falso_negativo = 0
                erros = 0

                for m in range(0, len(results)):

                    if (results[m] == testlabels[n][m]):
                        counter = counter + 1
                        if (results[m] == 1):
                            verd_positivo = verd_positivo + 1
                        if (results[m] == 0):
                            verd_negativo = verd_negativo + 1

                    if (results[m] != testlabels[n][m]):
                        erros = erros + 1
                        if (results[m] == 1):
                            falso_positivo = falso_positivo + 1
                        if (results[m] == 0):
                            falso_negativo = falso_negativo + 1

                    if (testlabels[n][m] == 1):
                        c = c + 1

                counter2 = 0
                for r in range(0, len(tra)):
                    if (traininglabels[n][r] == 1):
                        counter2 = counter2 + 1

                time2training = end_training - begining_training
                time2tranform = end_transform - begining_transform
                print('Time Elapsed(s):', (time2process + time2training + time2tranform))
                print('C:', C[l])
                print('Gamma:', gamma[g])
                print("Quant. de Ataques - Teste :", c)
                print("Quant. de Ataques - Training :", counter2)
                print("Quant. Ataques Total: ", c + counter2)
                print("Acertos: ", counter)
                print("Verd-Pos: ", verd_positivo)
                print("Verd-Neg: ", verd_negativo)
                print("Erros: ", len(results) - counter)
                print("Falso-Pos: ", falso_positivo)
                print("Falso-Neg: ", falso_negativo)
                print("Taxa de Acertos:", counter / len(results), "\n\n")

### --- End RBF
'''
## ------------ Poly
print('Poly')
for n in range(0,randomlist.nTest):
    print('Test:', n)

    min_max_scaler = preprocessing.MinMaxScaler()
    tra = min_max_scaler.fit_transform(training[n])
    tst = min_max_scaler.fit_transform(test[n])
    for c in range(0, len(components)):
        begining_transform = datetime.now()
        print('n_components:',components[c])
        pca=PCA(n_components=components[c])
        pca.fit(tra)
        tra = pca.transform(tra)
        tst = pca.transform(tst)
        end_transform = datetime.now()
        for l in range(0,len(C)):
            for d in range(0,len(degree)):
                begining_training = datetime.now()
                clf = svm.SVC(C=C[l],kernel='poly',random_state=1,class_weight={0:1,1:3},degree=degree[d])
                clf.fit(tra, traininglabels[n])
                results = clf.predict(tst)
                end_training = datetime.now()

                counter = 0
                c = 0
                verd_positivo = 0
                verd_negativo = 0
                falso_positivo = 0
                falso_negativo = 0
                erros = 0

                for m in range(0, len(results)):

                    if (results[m] == testlabels[n][m]):
                        counter = counter + 1
                        if (results[m] == 1):
                            verd_positivo = verd_positivo + 1
                        if (results[m] == 0):
                            verd_negativo = verd_negativo + 1

                    if (results[m] != testlabels[n][m]):
                        erros = erros + 1
                        if (results[m] == 1):
                            falso_positivo = falso_positivo + 1
                        if (results[m] == 0):
                            falso_negativo = falso_negativo + 1

                    if (testlabels[n][m] == 1):
                        c = c + 1

                counter2 = 0
                for r in range(0, len(tra)):
                    if (traininglabels[n][r] == 1):
                        counter2 = counter2 + 1

                time2training = end_training - begining_training
                time2tranform = end_transform - begining_transform
                print('Time Elapsed(s):', (time2process + time2training + time2tranform))
                print('C:', C[l])
                print('Degree:', degree[d])
                print("Quant. de Ataques - Teste :", c)
                print("Quant. de Ataques - Training :", counter2)
                print("Quant. Ataques Total: ", c + counter2)
                print("Acertos: ", counter)
                print("Verd-Pos: ", verd_positivo)
                print("Verd-Neg: ", verd_negativo)
                print("Erros: ", len(results) - counter)
                print("Falso-Pos: ", falso_positivo)
                print("Falso-Neg: ", falso_negativo)
                print("Taxa de Acertos:", counter / len(results), "\n\n")

### --- End Linear

