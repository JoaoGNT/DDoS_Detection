import csv
import ipaddress
from datetime import datetime


file = 'C:/Users/jg_te/Documents/Datasets/UNB CICIDS2017/TrafficLabelling/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv'
flow = []
numLines = 0
convertedFlow = []
d = []
data = []
dateVector = []
with open(file,'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dateVector.append(row[6])
        del row[6]
        del row[0]
        numLines=numLines+1
        flow.append(row)

numAttributes = len(flow[0])
data = flow[1:numLines]
dateVector = dateVector[1:numLines]
numLines = len(data)

for k in range (0, numLines):
    dateVector[k]=datetime.strptime(dateVector[k],'%d/%m/%Y %H:%M')


for a in range(0, numLines):
    data[a][0] = int(ipaddress.ip_address(data[a][0]))
    data[a][2] = int(ipaddress.ip_address(data[a][2]))

    if data[a][numAttributes - 1] == 'BENIGN':
        data[a][numAttributes - 1] = -1
    else:
        data[a][numAttributes - 1] = 1

    for b in range(1, numAttributes - 1):
        data[a][b] = float(data[a][b])

data = data

def lista_simples(lista):
    if isinstance(lista, list):
        return [sub_elem for elem in lista for sub_elem in lista_simples(elem)]
    else:
        return [lista]



