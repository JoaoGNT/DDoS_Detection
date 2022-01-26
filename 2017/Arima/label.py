import csvReader

#-------------------------------- STEP 1 -----------------------------------------#
''' Scope
    *Initiallizing variables
    *Establihing the sliding window code to -- vector named as vector is the final vector 
'''

label = csvReader.label
for r in range(0, len(csvReader.label)):
    if label[r] == 'BENIGN':
        label[r] = 0
    else:
        label[r] = 1


def lista_simples(lista):
    if isinstance(lista, list):
        return [sub_elem for elem in lista for sub_elem in lista_simples(elem)]
    else:
        return [lista]

delta = 1 #sliding window
wSize = 5 #window size
window = [] #window vector
minuteVecWindow = []
d0 = csvReader.dateVector[0] #first date data
BckBytesIndex = 7  #backward packets index

for time in range(0, len(csvReader.dateVector)):
    window.append(label[time])
    if (csvReader.dateVector[time].hour*60+ csvReader.dateVector[time].minute - d0.hour*60-d0.minute == delta):
        minuteVecWindow.append(window)
        d0 = csvReader.dateVector[time]
        window = []
labelswindows =[]
for t in range(wSize,len(minuteVecWindow)):
    vec = minuteVecWindow[t-wSize:t+1]
    labelswindows.append(lista_simples(vec))

print(len(labelswindows))
print(len(labelswindows[0]))
print(len(labelswindows[1]))
print(labelswindows[0])