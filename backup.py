import csv

class csvReader():
    file = 'C:/Users/Windows 10/Documents/Dataset TCC/Datasets/UNB CICIDS2017/TrafficLabelling/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv'
    destPort = []
    numLines = 0
    counter = 1
    counter2 = 0
    normalData = []

    with open(file,'r') as csvfile:
        reader = csv.reader(csvfile)
        #next(reader)
        for row in reader:
            numLines=numLines+1
            dp = row
            destPort.append(dp)

    lenFlow = len(destPort[0])
    print('Quantidade de atributos: ',lenFlow)
    print('Número de linhas/fluxos: ',numLines)


    for counter in range(1,numLines):
        flow = destPort[counter]
        normalFlow = []
        for counter2 in range(0,lenFlow-1):
            flow[counter2] = float(flow[counter2])
            normalFlow.append(flow[counter2])
            normalData.append(normalFlow)

pass

lengthTrain = round(csvReader.lenFlow*(2/3))
class trainData():
    trainData = []
    for i in range(0,lengthTrain):
        trainData.append(csvReader.normalData[i])
pass

class testData():
    testData = []
    for i in range(lengthTrain+1,csvReader.lenFlow):
        testData.append(csvReader.normalData[i])
    pass
