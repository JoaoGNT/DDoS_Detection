import csv
import ipaddress

class csvReader():
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

    # print(flow[0])
    # print(type(flow[0][0]))
    numAttributes = len(flow[0])
    # print('Number of Attributes: ', numAttributes)
    # print('NÃºmero de linhas/fluxos: ', numLines)


    for a in range(1, numLines):
        flow[a][0] = int(ipaddress.ip_address(flow[a][0]))
        flow[a][2] = int(ipaddress.ip_address(flow[a][2]))

        if flow[a][numAttributes-1] == 'BENIGN':
            flow[a][numAttributes-1] = -1
        else:
            flow[a][numAttributes-1] = 1

        for b in range(1, numAttributes-1):
            flow[a][b] = float(flow[a][b])

    data = flow[1:numLines]
pass

# print(csvReader.flow[0])
# print(csvReader.data[0])
# print(csvReader.data[len(csvReader.data)-1])


