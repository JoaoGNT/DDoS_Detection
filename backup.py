import csv
import ipaddress
from scipy.stats import entropy
from collections import Counter


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

print('Dados: ',data)

totalPacketsFwd = []
window = 5
tempo = []
time = 0
totalPacketsFwdProbability = []
totalPacketsFwdEntropyVec= []
counts = 0
total = 0
for line in range(0, len(data)):
    totalPacketsFwd.append(data[line][6])
    tempo.append(data[line][5])
print('Pacotes Foward: ',totalPacketsFwd)
print('Duração do fluxo (s): ',tempo)
Lista = []
for line in range (0,len(data)):

    time = time + data[line][5]

    if time >= window:
        counts = Counter(totalPacketsFwd)
        print(counts)
        print(counts.items())
        total = sum(list(counts.values()))
        probability_mass = {k: v/total for k, v in counts.items()}
        probabilityList = list(probability_mass.values())
        Lista.append(probabilityList)
        totalPacketsFwdEntropy = entropy(probabilityList)
        totalPacketsFwdEntropyVec.append(totalPacketsFwdEntropy)
        time = 0
        counts = 0
        total = 0



# print(totalPacketsFwd)
# print(probabilityList)
# print(Lista)
# print(time)
# print(totalPacketsFwdEntropyVec)

