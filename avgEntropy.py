import fwdPktEntropy
import bckPktEntropy
import fwdBytesEntropy
import bckBytesEntropy
import csvReader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math

avgVec = []
for c in range(0,len(fwdPktEntropy.totalPacketsFwdEntropyVec)):
    avgEntropy = (fwdPktEntropy.totalPacketsFwdEntropyVec[c] + bckPktEntropy.totalPacketsBckEntropyVec[c]
                  + fwdBytesEntropy.totalBytesFwdEntropyVec[c] + bckBytesEntropy.totalBytesBckEntropyVec[c])/4
    avgVec.append(avgEntropy)

print(avgVec)
print(len(avgVec))

### ----- Duration Vector ----- ###

w = 5
window = []
timevectorWindow = []
d0 = csvReader.dateVector[0]
for time in range(0,len(csvReader.dateVector)):
    if (csvReader.dateVector[time].hour == d0.hour):
        if (csvReader.dateVector[time].minute - d0.minute == 5):
            timevectorWindow.append(csvReader.dateVector[time])
            d0 = csvReader.dateVector[time]
            window = []
    else:
        timevectorWindow.append(csvReader.dateVector[time])
        d0 = csvReader.dateVector[time]
        window = []
timevectorWindow.append(csvReader.dateVector[len(csvReader.dateVector)-1])

# print(timevectorWindow)
# print(len(timevectorWindow))

### ----- End Duration Vector ----- ###



### ----- Time Series Analisys ----- ###


dataFrame = pd.DataFrame(avgVec,index=timevectorWindow)
arimaData = dataFrame[0:4]
# print(arimaData)
model = sm.tsa.SARIMAX(arimaData, order=(1, 0, 0), trend='c')
res = model.fit()
forecast = res.forecast(steps=15)
#
# print(forecast)
# print()
# print(forecast[0])
# plt.plot(dataFrame)
# plt.plot(forecast)
# plt.show()


### ----- End Time Series Analisys ----- ###

### ----
#
# print(arimaData)
# print(dataFrame)
# print(dataFrame[0])
# print(dataFrame.loc[timevectorWindow[1]])
# print(forecast)

# print(len(data2l))
# print(len(forecast))
# print(forecast[2])
# print(data2l[0])

LuVector = []
LdVector = []
Vu=[]
errorVector = []
for r in range(0,len(forecast)):
    error = dataFrame.loc[timevectorWindow[r+4]]-forecast[r]
    errorVector.append(error)

# print('Error:',errorVector[0])
# print('Error:',errorVector[1])
# print(errorVector[0]+errorVector[1])

var = np.var(errorVector)
# print(var)
for k in range(0,len(forecast)):
    Lu = forecast[k]+math.sqrt(var)
    Ld = forecast[k]-math.sqrt(var)
    LuVector.append(Lu)
    LdVector.append(Ld)

print(LuVector)
print(LdVector)

indexVec = []

print(type(dataFrame.loc[timevectorWindow[4]]))

'''
for j in range(0,len(forecast)):

    if LdVector[j]<dataFrame.loc[timevectorWindow[j+4]]<LdVector[j]:
      q = 0
    else:
        indexVec.append(dataFrame.index)

print(indexVec)
'''



# for r in range(0,len(forecast)):