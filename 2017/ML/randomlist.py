training = []
trainingLabels= []
nTest = 5 #number of random lists == number of tests
nSample = 10000

with open('RandomL.txt', 'r') as f:
    randomlist = f.read()

randomlist = randomlist.replace("]","")
randomlist = randomlist.replace("[","")
randomlist = randomlist.split(",")

rl = []

for i in range(0,len(randomlist)):
    rl.append(int(randomlist[i]))

RList = []
counter = 0
for k in range (1, nTest+1):
    RList.append(rl[counter:nSample*k])
    counter = nSample*k


