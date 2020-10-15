import csv
import ipaddress
from scipy.stats import entropy
from collections import Counter
import csvReader


file = 'C:/Users/Windows 10/Documents/Dataset TCC/Datasets/UNB CICIDS2017/TrafficLabelling/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv'
flow = []
numLines = 0
convertedFlow = []
d = []
data = []
with open(file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        del row[6]
        del row[0]


        flow.append(row)

flow = flow[0:15]
numAttributes = len(flow[0])
numLines = len(flow)

for a in range(1, numLines):
    flow[a][0] = int(ipaddress.ip_address(flow[a][0]))
    flow[a][2] = int(ipaddress.ip_address(flow[a][2]))

    if flow[a][numAttributes - 1] == 'BENIGN':
        flow[a][numAttributes - 1] = -1
    else:
        flow[a][numAttributes - 1] = 1

    for b in range(1, numAttributes - 1):
        flow[a][b] = float(flow[a][b])

data = flow[1:numLines]

print(data[0])
print(csvReader.data[0])
#print('Quantidade de fluxos de dados:', len(data))


totalPacketsFwd = []
w = 300
tempo = []
time = 0
counts = 0
total = 0
for line in range(0, len(data)):
    totalPacketsFwd.append(data[line][6])
    tempo.append(data[line][5])
#print('Pacotes Foward: ',totalPacketsFwd)
#print('Duração do fluxo (s): ',tempo)

window = []
vectorWindow = []
for line in range (0,len(data)):

    time = time + data[line][5]
    window.append(data[line][6])
    if time >= w:
        vectorWindow.append(window)
        time = 0
        counts = 0
        total = 0
        window = []
length = 0
for r in range (0,len(vectorWindow)):
    length = len(vectorWindow[r]) + length

if length != len(data):
    for l in range(0, len(data)):
        lastWindow = data[length:len(data)]

    for q in range(0, len(lastWindow)):
        last_attributes = lastWindow[q][6]
        vectorWindow.append([last_attributes])

totalPacketsFwdProbability = []
totalPacketsFwdEntropyVec= []
probabilityList = []
diffValuesVec = []
#print(vectorWindow)
for a in range(0,len(vectorWindow)):
    counts = Counter(vectorWindow[a])
    # print(counts)
    # print(counts.items())
    total = sum(list(counts.values()))
    probability_mass = {k: v/total for k, v in counts.items()}
    probability = list(probability_mass.values())
    probabilityList.append(probability)
    diffValues = len(counts.items())
    diffValuesVec.append(diffValues)

# print(diffValuesVec)
# print(probabilityList)

for m in range (0,len(probabilityList)):
   if diffValuesVec[m] == 1:
        totalPacketsFwdEntropy = 0
        totalPacketsFwdEntropyVec.append(totalPacketsFwdEntropy)
   else:
        totalPacketsFwdEntropy = entropy(probabilityList[m], base=diffValuesVec[m])
        totalPacketsFwdEntropyVec.append(totalPacketsFwdEntropy)

# print(totalPacketsFwdEntropyVec)
print(numAttributes)


