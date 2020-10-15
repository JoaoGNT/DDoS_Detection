import csv
import ipaddress


file = 'C:/Users/Windows 10/Documents/Dataset TCC/Datasets/UNB CICIDS2017/TrafficLabelling/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv'
flow = []
numLines = 0
convertedFlow = []
d = []
data = []
with open(file,'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        del row[6]
        del row[0]
        numLines=numLines+1
        flow.append(row)
# print(flow[1])
# print(flow[numLines-1])
# print(flow[0])
# print(type(flow[0][0]))
numAttributes = len(flow[0])
# print('Number of Attributes: ', numAttributes)
# print('NÃºmero de linhas/fluxos: ', numLines)

data = flow[1:numLines]

numLines = len(data)
# print(data[0])
# print(data[numLines-1])
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
# print(data[0])
# print(data[numLines-1])



