from scipy.stats import entropy
from collections import Counter
import csvReader
import datetime

def lista_simples(lista):
    if isinstance(lista, list):
        return [sub_elem for elem in lista for sub_elem in lista_simples(elem)]
    else:
        return [lista]

t = 1 #minutes
window = []
minuteVecWindow = []
d0 = csvReader.dateVector[0]
for time in range(0,len(csvReader.dateVector)):
    window.append(csvReader.data[time][8])
    if (csvReader.dateVector[time].hour*60+csvReader.dateVector[time].minute - d0.hour*60-d0.minute == t):
        minuteVecWindow.append(window)
        d0 = csvReader.dateVector[time]
        window = []
vector =[]
for t in range(5,len(minuteVecWindow)):
    vec = minuteVecWindow[t-5:t+1]
    vector.append(lista_simples(vec))

twindow = csvReader.dateVector[0] + datetime.timedelta(minutes=5)
dateVec = []
dateVec.append(twindow)

# print(vector[2][0][0])
# print(len(vector[2][0]))
# print(type(vector[2][0]))



totalBytesFwdEntropy = []
totalBytesFwdEntropyVec= []
probabilityList = []
diffValuesVec = []
#print(vectorWindow)
for a in range(0,len(vector)):
    counts = Counter(vector[a])
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

# print(totalBytesFwdEntropyVec)
