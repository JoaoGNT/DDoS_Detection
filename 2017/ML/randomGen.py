import random
import csvReader
import json

nTest = 5 #number of random lists == number of tests
nSample = 10000
randomL=[]
# randomlist = sorted(random.sample(range(0, len(csvReader.data)), nSample))

for i in range(0,nTest):
    randomlist = []
    randomlist = sorted(random.sample(range(0, len(csvReader.data)), nSample))
    randomL.append(randomlist)

with open('RandomL.txt', 'w') as f:
    f.write(json.dumps(randomL))
