from scipy.stats import entropy
from collections import Counter
import csvReader

w = 5
window = []
vectorWindow = []

for time in range(0,len(csvReader.dateVector)):
    window.append(csvReader.data[time][8])
    if (csvReader.dateVector[time].minute - csvReader.d0 == 5):
        vectorWindow.append(window)
        d0 = csvReader.dateVector[time].minute
        window = []
length =0
for r in range (0,len(vectorWindow)):
    length = len(vectorWindow[r]) + length

lastWindowVector= []
if length != len(csvReader.data):
    for l in range(0, len(csvReader.data)):
        lastWindow = csvReader.data[length:len(csvReader.data)]

    for q in range(0, len(lastWindow)):
        last_attributes = lastWindow[q][8]
        lastWindowVector.append(last_attributes)
vectorWindow.append(lastWindowVector)


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

# print(vectorWindow[0])
# print(len(totalBytesFwdEntropyVec))
# print(len(csvReader.data))
# print(w)
