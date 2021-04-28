''' General Scope
This script has as main goal calculate
'''

from Arima import bckBytesEntropy, csvReader, bckPktEntropy, fwdBytesEntropy, fwdPktEntropy
import datetime
import pandas as pd

import statsmodels.api as sm

#-------------------------------- STEP 1 -----------------------------------------#
''' Scope
    * Calculate the average entropy of the four attributes
'''

avgVec = []
for c in range(0, len(fwdPktEntropy.totalPacketsFwdEntropyVec)):
    avgEntropy = (fwdPktEntropy.totalPacketsFwdEntropyVec[c] + bckPktEntropy.totalPacketsBckEntropyVec[c]
                  + fwdBytesEntropy.totalBytesFwdEntropyVec[c] + bckBytesEntropy.totalBytesBckEntropyVec[c]) / 4
    avgVec.append(avgEntropy)

# print(avgVec)
# print(len(avgVec))

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
for s in range(0, len(fwdPktEntropy.minuteVecWindow) - 6):
    twindow = twindow + datetime.timedelta(minutes=delta)
    dateVec.append(twindow)

# print(dateVec)
# print(len(dateVec))
# print(timevectorWindow)
# print(len(timevectorWindow))
#-------------------------------- END STEP 2 -----------------------------------------#

#-------------------------------- STEP 3 -----------------------------------------#
''' Scope
    * Creating the duration vector
    * x axis for the graphs
'''

step = 5
forecastWindow = 5
dataFrame = pd.DataFrame(avgVec,index=dateVec)
arimaData = dataFrame[0:forecastWindow]
print(arimaData)

step = 5
forecastWindow = 5 # this is the window size used to forcast the next windows
dataFrame = pd.DataFrame(avgVec,index=dateVec) # building the dataframe linking the average entropy with the timestamp
arimaData = dataFrame[0:forecastWindow] #
model = sm.tsa.SARIMAX(arimaData, order=(1, 1, 1), trend='c')
res = model.fit()
forecast = res.forecast(steps=step)

print("")
print("")
print("")
print("")
print(forecast)