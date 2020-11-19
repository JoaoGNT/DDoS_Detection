import fwdPktEntropy
import bckPktEntropy
import fwdBytesEntropy
import bckBytesEntropy
import datetime
import pandas as pd
import csvReader
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
# print(len(avgVec))

### ----- Duration Vector ----- ###
dateVec =[]
twindow = csvReader.dateVector[0] + datetime.timedelta(minutes=5)
dateVec = []
dateVec.append(twindow)
for s in range(0,len(fwdPktEntropy.minuteVecWindow)-6):
    twindow = twindow + datetime.timedelta(minutes=1)
    dateVec.append(twindow)

# print(dateVec)
# print(len(dateVec))
# print(timevectorWindow)
# print(len(timevectorWindow))

### ----- End Duration Vector ----- ###



### ----- Time Series Analisys ----- ###
step = 5
forecastWindow = 5
dataFrame = pd.DataFrame(avgVec,index=dateVec)

arimaData = dataFrame[0:forecastWindow]
# print(arimaData)
model = sm.tsa.SARIMAX(arimaData, order=(1, 1, 1), trend='c')
res = model.fit()
forecast = res.forecast(steps=step)
# print(forecast)
# plt.plot(dataFrame[4:len(dataFrame)])


### ----- End Time Series Analisys ----- ###

### ----

'''
LuVector = []
LdVector = []
Vu=[]

# print('Error:',errorVector[0])
# print('Error:',errorVector[1])
# print(errorVector[0]+errorVector[1])

#var = np.var(errorVector)
var = np.var(arimaData)
# print(var)
for k in range(0,len(forecast)):
    Lu = forecast[k]+1.96*math.sqrt(var)
    Ld = forecast[k]-1.96*math.sqrt(var)
    LuVector.append(Lu)
    LdVector.append(Ld)
'''
errorVector = []
# print(dataFrame)
# print(dateVec)


for r in range(0,len(forecast)):

    error = dataFrame.loc[dateVec[r+step]]-forecast[r]
    errorVector.append(error)

var = np.var(errorVector)
############
limiara =[]
limiarb=[]
print(len(forecast))

for n in range(0,len(forecast)):
    limiarUp = forecast[n] + 1.96 * math.sqrt(var)
    limiara.append(limiarUp)
    limiarDown = forecast[n] - 1.96 * math.sqrt(var)
    limiarb.append(limiarDown)

print(limiara)
print(limiarb)
# limiarVecUp = []
# limiarVecDown = []

limiarVecUp = np.resize(limiara,(1,(len(dataFrame)-(forecastWindow+step))))
limiarVecDown = np.resize(limiarb,(1,(len(dataFrame)-(forecastWindow+step))))
# print(limiarVecUp)

#################
'''
limiarUp = forecast[0] + 1.96*math.sqrt(var)
limiarDown = forecast[0] - 1.96*math.sqrt(var)
limiarVecUp = []
limiarVecDown = []
for n in range(0,len(dataFrame)-(forecastWindow+step)):
    limiarVecUp.append(limiarUp)
    limiarVecDown.append(limiarDown)
# print(len(limiarVecUp))
# print(limiarVecUp)
# print(dateVec[forecastWindow+step:len(dataFrame)])
# print(len(dateVec[forecastWindow+step:len(dataFrame)]))
'''
limiarUp = pd.DataFrame(limiarVecUp.T,index=dateVec[forecastWindow+step:len(dataFrame)])
limiarDown = pd.DataFrame(limiarVecDown.T,index=dateVec[forecastWindow+step:len(dataFrame)])
print(errorVector)
print(limiarVecUp)
print(var)
df = dataFrame[forecastWindow+step:len(dataFrame)]
dv = dateVec[forecastWindow+step:len(dataFrame)]
print(limiarUp)
print()
print()
# print(dv)

## -----
index =[]
ns=0
nss=0

result = np.where(((df > limiarUp) | (df < limiarDown)),'True', 'False')

print(result)
print(len(result))
print(result[0][0])
print(type(result))
print(type(result[0][0]))
dt = []
for n in range(0,len(result)):
    if (result[n][0] == 'True'):
        dt.append(df.loc[dv[n]])
        ns = ns+1
    else:
        nss = nss + 1
print('Selecionadas:', ns)
print('Não Selecionadas:', nss)

'''
for r in range(0,len(limiarVecUp)):

    if abs(df.loc[dv[r]]>limiarUp.loc[dv[r]]) | abs(df.loc[dv[r]]<limiarDown.loc[dv[r]]):
        index.append(r)
        ns = ns+1
    else:
        nss = nss+1

'''
plt.plot(df)
plt.plot(limiarUp)
plt.plot(limiarDown)
plt.xlabel('Time')
plt.xlabel('Normalized Entropy')
plt.show()