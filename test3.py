import datetime
import pandas as pd
import numpy as np

b = [0.00523,0.000476,-0.00258,-0.006329]
a=np.resize(b,(1,7))

limiarUp = pd.DataFrame(a).T
print(limiarUp)


dateVector = [datetime.datetime(year=2017,month=7,day=7,hour=3,minute=50,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=3,minute=51,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=3,minute=52,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=3,minute=53,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=3,minute=54,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=3,minute=55,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=3,minute=56,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=3,minute=57,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=3,minute=58,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=3,minute=59,second=0),
datetime.datetime(year=2017,month=7,day=7,hour=4,minute=0,second=0),
datetime.datetime(year=2017, month=7, day=7, hour=4, minute=1, second=0),
datetime.datetime(year=2017, month=7, day=7, hour=4, minute=2, second=0),
datetime.datetime(year=2017, month=7, day=7, hour=4, minute=3, second=0),
datetime.datetime(year=2017, month=7, day=7, hour=4, minute=4, second=0),
datetime.datetime(year=2017, month=7, day=7, hour=4, minute=5, second=0),
datetime.datetime(year=2017, month=7, day=7, hour=4, minute=6, second=0)]

print(len(dateVector))
data= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]



dataFrame = pd.DataFrame(data, index=dateVector)
print(dataFrame)
print(dataFrame.loc[dateVector[0]])
print(type(dataFrame.loc[dateVector[1]]))
# print(type(dateVector[0].hour))
# print(dateVector[0].minute)
# window = []
# vectorWindow =[]
# d0 = dateVector[0]
# print(d0.hour)
# w = 5
# for c in range(0,len(dateVector)):
#     window.append(data[c])
#
#     if (dateVector[c].hour*60 + dateVector[c].minute - d0.hour*60-d0.minute == 5):
#         vectorWindow.append(window)
#         d0 = dateVector[c] - datetime.timedelta(minutes=4)
#         window = []
#         c=0
#
#
# print(vectorWindow)
# length = 0
# for r in range (0,len(vectorWindow)):
#     length = len(vectorWindow[r]) + length
#
# lastWindowVector= []
# if length != len(data):
#     for l in range(0, len(data)):
#         lastWindow = data[length:len(data)]
#
#     for q in range(0, len(lastWindow)):
#         last_attributes = lastWindow[q]
#         lastWindowVector.append(last_attributes)
# vectorWindow.append(lastWindowVector)
# print(vectorWindow)
#
# print(length)