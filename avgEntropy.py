import fwdPktEntropy
import bckPktEntropy
import fwdBytesEntropy
import bckBytesEntropy
import csvReader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

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
print(arimaData)
model = sm.tsa.SARIMAX(arimaData, order=(1, 0, 0), trend='c')
res = model.fit()
forecast = res.forecast(steps=15)
print(forecast)
plt.plot(dataFrame)
plt.plot(forecast)
plt.show()


# tsAnalysis = tsAnalysis.holt_winters(avgVec[0:4],2,15)






