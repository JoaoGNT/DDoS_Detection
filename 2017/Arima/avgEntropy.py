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
import label
#from datetime import datetime

#-------------------------------- STEP 1 -----------------------------------------#
''' Scope
    * Calculate the average entropy of the four attributes
'''

avgVec = []
for c in range(0, len(fwdPktEntropy.totalPacketsFwdEntropyVec)):
    avgEntropy = (fwdPktEntropy.totalPacketsFwdEntropyVec[c] + bckPktEntropy.totalPacketsBckEntropyVec[c]
                  + fwdBytesEntropy.totalBytesFwdEntropyVec[c] + bckBytesEntropy.totalBytesBckEntropyVec[c]) / 4
    avgVec.append(avgEntropy)

print(avgVec)
print(len(avgVec))

#-------------------------------- END STEP 1 -----------------------------------------#

# -------------------------------- STEP 2 -----------------------------------------#
''' Scope
    * Creating the duration vector
    * x axis for the graphs
'''
wSize = 5  # window size
delta = 1  # sliding window delta
dateVec = []  # x axis
twindow = csvReader.dateVector[0] + datetime.timedelta(minutes=wSize)  # 1st date in csv + 5min = the end of the first window
dateVec.append(twindow)  # appending the first date window value
for s in range(0, len(fwdPktEntropy.minuteVecWindow) - 6):
    twindow = twindow + datetime.timedelta(minutes=delta)
    dateVec.append(twindow)

# print(dateVec)
# print(len(dateVec))
# print(timevectorWindow)
# print(len(timevectorWindow))
# -------------------------------- END STEP 2 -----------------------------------------#

# -------------------------------- STEP 3 -----------------------------------------#
''' Scope
    * bulding the data frame used to establish the Arima model
    * creating and fiting the model
    * doing the forecast
'''

step = 5  # how many windows will be forecasted
forecastWindow = 5  # this is the window size used to forcast the next windows
dataFrame = pd.DataFrame(avgVec, index=dateVec)  # building the dataframe linking the average entropy with the timestamp
arimaData = dataFrame[0:forecastWindow]  # building the data that wil be used to establish the Arima Model
# model_order = [(1,1,1),(2,1,1),(1,2,1),(1,1,2),(2,2,1),(1,2,2),(2,1,2),(2,2,2),(5,1,1),(1,5,1),(1,1,5),(5,5,5)]
model_order = [(1, 1, 1), (2, 1, 1), (3, 1, 1), (1, 1, 2), (2, 1, 2), (3, 1, 2),
               (1, 1, 3), (2, 1, 3), (3, 1, 3), (1, 2, 1), (2, 2, 1), (3, 2, 1),
               (1, 2, 2), (2, 2, 2), (3, 2, 2), (1, 2, 3), (2, 2, 3), (3, 2, 3), (1, 3, 1),
               (2, 3, 1), (3, 3, 1), (1, 3, 2), (2, 3, 2), (3, 3, 2), (1, 3, 3), (2, 3, 3),(3,3,3)]


vecacertos = []
vecerros = []
vecfalso_positivo = []
vecverd_positivo = []
vecfalso_negativo = []
vecverd_negativo = []
vectaxa_acerto = []
order = []
time = []
for mod in range(0, len(model_order)):
    start_time = datetime.datetime.now()
    model = sm.tsa.arima.ARIMA(arimaData, order=model_order[mod])
    res = model.fit()  # fitting the model
    forecast = res.forecast(steps=step)  # forecasting
    # -------------------------------- END STEP 3 -----------------------------------------#

    # -------------------------------- STEP 3 -----------------------------------------#
    ''' Scope
        * establishing thresholds -- up and down

    '''
    errorVector = []
    tshVecup = []  # vector with the up thresholds
    tshVecdown = []  # vector with the down thresholds
    end_time = datetime.datetime.now()
    for r in range(0, len(forecast)):
        error = dataFrame.loc[dateVec[r + step]] - forecast[r]  # error = the real value - forecast for that value
        errorVector.append(error)  # composing the vector with errors
    var = np.var(errorVector)  # calculating the variance in errorVector

    for ind in range(0, len(forecast)):  # building a vector with the threshold
        tshUp = forecast[ind] + 1.96 * math.sqrt(var)
        tshVecup.append(tshUp)
        tshDown = forecast[ind] - 1.96 * math.sqrt(var)
        tshVecdown.append(tshDown)

    tshVecup = np.resize(tshVecup, (1, (len(dataFrame) - (forecastWindow + step))))  # reshaping both vectors
    tshVecdown = np.resize(tshVecdown, (1, (len(dataFrame) - (forecastWindow + step))))
    tshUp = pd.DataFrame(tshVecup.T, index=dateVec[forecastWindow + step:len(dataFrame)])  # building the DataFrame with both thresholds
    tshDown = pd.DataFrame(tshVecdown.T, index=dateVec[forecastWindow + step:len(dataFrame)])

    df = dataFrame[forecastWindow + step:len(dataFrame)]
    dv = dateVec[forecastWindow + step:len(dataFrame)]
    # -------------------------------- STEP 4 -----------------------------------------#
    ''' Scope
        * script - compare if it happened an attack during the window

    '''
    index = []
    ns = 0
    nss = 0
    # result = np.where(((df > tshUp) | (df < tshDown)), 'True', 'False')
    result = np.where(df < tshDown, 'True', 'False')
    dt = []
    window_atack = []
    window_normal = []
    for n in range(0, len(result)):
        if (result[n][0] == 'True'):
            dt.append(df.loc[dv[n]])
            ns = ns + 1
            window_atack.append(n)
        else:
            window_normal.append(n)
            nss = nss + 1
    # print('Ataque:', ns)
    # print('Normal:', nss)
    # print(window_atack)
    # -------------------------------- END STEP 4 -----------------------------------------#

    # ------------------------------- STEP 5 ---------------------------------------------#
    '''
    Metrics
    '''

    acertos_atack = 0
    erros_atack = 0
    for k in range(0, len(window_atack) - 1):
        for t in range(0, len(label.labelswindows[window_atack[k]])):
            if (label.labelswindows[window_atack[k]][t] == 1):
                acertos_atack = acertos_atack + 1
            else:
                erros_atack = erros_atack + 1

    acertos_normal = 0
    erros_normal = 0
    for r in range(0, len(window_normal) - 1):
        for v in range(0, len(label.labelswindows[window_normal[r]])):
            if (label.labelswindows[window_normal[r]][v] == 0):
                acertos_normal = acertos_normal + 1
            else:
                erros_normal = erros_normal + 1

    acertos = acertos_normal + acertos_atack
    erros = erros_atack + erros_normal
    taxa_acerto = (acertos_normal + acertos_atack) * 100 / (acertos_normal + acertos_atack + erros_atack + erros_normal)
    time.append(end_time-start_time)
    vecacertos.append(acertos)
    vecerros.append(erros)
    vecverd_positivo.append(acertos_atack)
    vecverd_negativo.append(acertos_normal)
    vecfalso_negativo.append(erros_normal)
    vecfalso_positivo.append(erros_atack)

    vectaxa_acerto.append(taxa_acerto)
    order.append(model.order)
    # -------------------------------- STEP 5 -----------------------------------------#
    ''' Scope
        * plotting
    '''
    plt.figure(figsize=(30,15))
    plt.rcParams.update({'font.size':40})
    plt.plot(df,marker='o',linewidth=5,markeredgewidth=9,label = "Janelas")
    plt.plot(tshDown,markeredgewidth=9,linewidth=5, label = "Limiar")
    plt.legend()
    plt.title(model.order)
    plt.xlabel('Tempo')
    plt.ylabel('Entropia')
    plt.savefig(','.join([str(value) for value in model.order]))
    plt.clf()
    # -------------------------------- END STEP 6 -----------------------------------------#

d = {'Order': model_order, 'Acertos': vecacertos, 'Erros': vecerros, 'Verdadeiro_Positivo': vecverd_positivo,
      'Verdadeiro_Negativo': vecverd_negativo, 'Falso_Positivo':vecfalso_positivo, 'Falso_Negativo':vecfalso_negativo,
     'Taxa de Acerto': vectaxa_acerto,'Time':time}
dataf = pd.DataFrame(d)
print(dataf)

with pd.ExcelWriter('metrics.xlsx') as writer:
    dataf.to_excel(writer)