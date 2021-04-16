''' General Scope
This script has as main goal calculate
'''

import fwdPktEntropy
import bckPktEntropy
import fwdBytesEntropy
import bckBytesEntropy
import datetime
import pandas as pd
import csvReader
import numpy as np
import statsmodels.api as sm
import math
import matplotlib.pyplot as plt

#-------------------------------- STEP 1 -----------------------------------------#
''' Scope
    * Calculate the average entropy of the four attributes
'''

avgVec = []
for c in range(0,len(fwdPktEntropy.totalPacketsFwdEntropyVec)):
    avgEntropy = (fwdPktEntropy.totalPacketsFwdEntropyVec[c] + bckPktEntropy.totalPacketsBckEntropyVec[c]
                  + fwdBytesEntropy.totalBytesFwdEntropyVec[c] + bckBytesEntropy.totalBytesBckEntropyVec[c])/4
    avgVec.append(avgEntropy)

print(avgVec)
print(len(avgVec))

#-------------------------------- END STEP 1 -----------------------------------------#

#-------------------------------- STEP 2 -----------------------------------------#
''' Scope
    * Creating the duration vector
    * x axis for the graphs
'''
wSize = 5 # window size
delta = 1 # sliding window delta
dateVec = [] # x axis
twindow = csvReader.dateVector[0] + datetime.timedelta(minutes=wSize) # 1st date in csv + 5min = the end of the first window
dateVec.append(twindow) #appending the first date window value
for s in range(0,len(fwdPktEntropy.minuteVecWindow)-6):
    twindow = twindow + datetime.timedelta(minutes=delta)
    dateVec.append(twindow)

print(dateVec)
print(len(dateVec))
# print(timevectorWindow)
# print(len(timevectorWindow))
#-------------------------------- END STEP 2 -----------------------------------------#

#-------------------------------- STEP 3 -----------------------------------------#
''' Scope
    * bulding the data frame used to establish the Arima model
    * creating and fiting the model
    * doing the forecast
'''

step = 5 # how many windows it'll be forecasted
forecastWindow = 5 # this is the window size used to forcast the next windows
dataFrame = pd.DataFrame(avgVec,index=dateVec) # building the dataframe linking the average entropy with the timestamp
arimaData = dataFrame[0:forecastWindow] # building the data that wil be used to establish the Arima Model
model = sm.tsa.SARIMAX(arimaData, order=(1, 1, 1), trend='c') #arima model
res = model.fit() #fitting the model
forecast = res.forecast(steps=step) #forecasting
#-------------------------------- END STEP 3 -----------------------------------------#

#-------------------------------- STEP 3 -----------------------------------------#
''' Scope
    * establishing thresholds -- up and down
    
'''
errorVector = []
tshVecup =[] # vector with the up thresholds
tshVecdown=[] # vector with the down thresholds

for r in range(0,len(forecast)):
    error = dataFrame.loc[dateVec[r+step]]-forecast[r] # error = the real value - forecast for that value
    errorVector.append(error) # composing the vector with errors
var = np.var(errorVector) # calculating the variance in errorVector

# print(len(forecast))

for n in range(0,len(forecast)): #building a vector with the threshold
    tshUp = forecast[n] + 1.96 * math.sqrt(var)
    tshVecup.append(tshUp)
    tshDown = forecast[n] - 1.96 * math.sqrt(var)
    tshVecdown.append(tshDown)


tshVecup = np.resize(tshVecup, (1, (len(dataFrame) - (forecastWindow + step)))) #reshaping both vectors
tshVecdown = np.resize(tshVecdown, (1, (len(dataFrame) - (forecastWindow + step))))
# print(tshVecup)
# print(tshVecdown)
tshUp = pd.DataFrame(tshVecup.T, index=dateVec[forecastWindow + step:len(dataFrame)]) #building the DataFrame with both thresholds
tshDown = pd.DataFrame(tshVecdown.T, index=dateVec[forecastWindow + step:len(dataFrame)])

df = dataFrame[forecastWindow+step:len(dataFrame)]
dv = dateVec[forecastWindow+step:len(dataFrame)]
# -------------------------------- STEP 4 -----------------------------------------#
''' Scope
    * script for compare if it happened an attack during the window

'''
index =[]
ns=0
nss=0
result = np.where(((df > tshUp) | (df < tshDown)), 'True', 'False')
dt = []
for n in range(0,len(result)):
    if (result[n][0] == 'True'):
        dt.append(df.loc[dv[n]])
        ns = ns+1
    else:
        nss = nss + 1
print('Selecionadas:', ns)
print('Não Selecionadas:', nss)
# -------------------------------- END STEP 4 -----------------------------------------#

# -------------------------------- STEP 5 -----------------------------------------#
''' Scope
    * plotting
'''
plt.plot(df)
plt.plot(tshUp)
plt.plot(tshDown)
plt.xlabel('Time')
plt.xlabel('Normalized Entropy')
plt.show()

# -------------------------------- END STEP 5 -----------------------------------------#