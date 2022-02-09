import pandas as pd
import re
datashape = {'Test':[],'Time(s)':[],'Architecture':[],'Alpha':[]}
dataset = pd.DataFrame(datashape)

with open('C:/Users/joao.teles/projects/DDoS_Detection/2017/ML/results/ANNresults.txt') as f:
    lines = f.readlines()
    
    for i in range(len(lines)):
        if re.match('.*Test:.*',lines[i]) != 'None':
            dataset.append(lines[i].split(':')[1])

print(dataset)



# import re

# string = 'Test: 0'

# str = 'abc'
# re.match('.*Test:.*', str)

# if re.match('.*Test:.*', string) != 'None':
#     print(string.split(':')[1])