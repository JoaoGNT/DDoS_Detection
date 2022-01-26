''' General Scope
This script has as his main goal transform and manipulate the data from csv databases
and at the end of this script have all the data that will be used along this work
'''
import csv
import ipaddress
from datetime import datetime

#-------------------------------- STEP 1 -----------------------------------------#
''' Scope
    *Initiallizing variables
    *Generating the flow vector without row 0 and 6 and a vector with de timestamps 
    *Both vectors are organized in the same way 
'''

file = 'C:/Users/jg_te/Documents/UFU/TCC/Datasets/2017/TrafficLabelling/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv'
flow = [] # vector to append data form the data base -- deleting rows 0 and 6 (flow ID and timestamp,respictively)
numLines = 0 # initializing a counter number of lines for vector flow
dateVector = [] # vector with the timestamp for each flow
label = []

with open(file,'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        label.append(row[84])
        dateVector.append(row[6])
        del row[6]
        del row[0]
        numLines=numLines+1
        flow.append(row)

label = label[1:numLines]
#-------------------------------- END STEP 1 ---------------------------------------#

#-------------------------------- STEP 2 -----------------------------------------#
''' Scope
    * Reshaping flow and dateVector  pulling out the first line (atribute's name line)
    * Reshaping dateVector to a specific date timestamp %d/%m/%Y %H:%M
'''

convertedFlow = []
d = [] #
numAttributes = len(flow[0])
data = flow[1:numLines] # flow - line 0 (line 0 coresponds to the flow's feature title (i.e. flow ID, ))
dateVector = dateVector[1:numLines]
numLines = len(data)

for k in range (0, numLines):
    dateVector[k]=datetime.strptime(dateVector[k],'%d/%m/%Y %H:%M') #this for changes the dateVector from str to timestamp type
#-------------------------------- END STEP 2 ---------------------------------------#

#-------------------------------- STEP 3 -----------------------------------------#
''' Scope
    * Converting ip addresses to int
    * Labeling data flows benigns as 1 and maligns as -1
    * Conveting all the the dat entries from data vector to float
'''

for a in range(0, numLines):
    data[a][0] = int(ipaddress.ip_address(data[a][0])) #17
    data[a][2] = int(ipaddress.ip_address(data[a][2])) #17

    if data[a][numAttributes - 1] == 'BENIGN':
        data[a][numAttributes - 1] = 0
    else:
        data[a][numAttributes - 1] = 1

    for b in range(1, numAttributes - 1):
        data[a][b] = float(data[a][b])

#-------------------------------- END STEP 3 ---------------------------------------#

data = data # final object

'''
def lista_simples(lista):
    if isinstance(lista, list):
        return [sub_elem for elem in lista for sub_elem in lista_simples(elem)]
    else:
        return [lista]
'''


