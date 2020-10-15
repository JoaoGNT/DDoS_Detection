from scipy.stats import entropy
from collections import Counter
import csvReader

w = 5*(10**6)
time = 0
counts = 0
total = 0
# for line in range(0, len(csvReader.data)):
#     totalBytesFwd.append(csvReader.data[line][8])
#     t.append(csvReader.data[line][5])
#print('Pacotes Foward: ',totalPacketsFwd)
#print('Duração do fluxo (s): ',tempo)

window = []
vectorWindow = []
for line in range (0,len(csvReader.data)):

    time = time + csvReader.data[line][5]
    window.append(csvReader.data[line][8])
    if time >= w:
        vectorWindow.append(window)
        time = 0
        counts = 0
        total = 0
        window = []
length = 0
for r in range (0,len(vectorWindow)):
    length = len(vectorWindow[r]) + length

if length != len(csvReader.data):
    for l in range(0, len(csvReader.data)):
        lastWindow = csvReader.data[length:len(csvReader.data)]

    for q in range(0, len(lastWindow)):
        last_attributes = lastWindow[q][8]
        vectorWindow.append([last_attributes])


totalBytesFwdEntropyVec= []
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

for m in range (0,len(probabilityList)):
   if diffValuesVec[m] == 1:
        totalBytesFwdEntropy = 0
        totalBytesFwdEntropyVec.append(totalBytesFwdEntropy)
   else:
        totalBytesFwdEntropy = entropy(probabilityList[m], base=diffValuesVec[m])
        totalBytesFwdEntropyVec.append(totalBytesFwdEntropy)
# print(len(totalBytesFwdEntropyVec))
# print(len(csvReader.data))
# print(w)
