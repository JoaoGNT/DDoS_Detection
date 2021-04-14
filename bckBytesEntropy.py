''' General Scope
This script returns a list composed by the backward bytes entropy for each flow window
'''

from scipy.stats import entropy
from collections import Counter
import csvReader
import datetime

#-------------------------------- STEP 1 -----------------------------------------#
''' Scope
    *Initiallizing variables
    *Establihing the sliding window code to -- vector named as vector is the final vector 
'''

def lista_simples(lista):
    if isinstance(lista, list):
        return [sub_elem for elem in lista for sub_elem in lista_simples(elem)]
    else:
        return [lista]

t = 1 #sliding window
wSize = 5 #window size
window = [] #window vector
minuteVecWindow = []
d0 = csvReader.dateVector[0] #first date data
BckBytesIndex = 9 #backward bytes index

for time in range(0,len(csvReader.dateVector)):
    window.append(csvReader.data[time][BckBytesIndex])
    if (csvReader.dateVector[time].hour*60+csvReader.dateVector[time].minute - d0.hour*60-d0.minute == t):
        minuteVecWindow.append(window)
        d0 = csvReader.dateVector[time]
        window = []
vector =[]
for t in range(wSize,len(minuteVecWindow)):
    vec = minuteVecWindow[t-wSize:t+1]
    vector.append(lista_simples(vec))

#-------------------------------- END STEP 1 -----------------------------------------#

# twindow = csvReader.dateVector[0] + datetime.timedelta(minutes=wSize)
# dateVec = []
# dateVec.append(twindow)
# print(dateVec)

#-------------------------------- STEP 2 -----------------------------------------#
''' Scope
    *Calculating the entropy related to the backward bytes in each time window
'''

totalBytesBckEntropy = [] #
totalBytesBckEntropyVec= [] #vector for the entropy related to the window
probabilityList = [] #probability list compose of the propability of each value o bck bytes inside
diffValuesVec = [] #vector to append the different values

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
        totalBytesBckEntropy = 0
        totalBytesBckEntropyVec.append(totalBytesBckEntropy)
   else:
        totalBytesBckEntropy = entropy(probabilityList[m], base=diffValuesVec[m])
        totalBytesBckEntropyVec.append(totalBytesBckEntropy)

print(len(totalBytesBckEntropyVec))
print(len(vector))

#-------------------------------- END STEP 2 -----------------------------------------#