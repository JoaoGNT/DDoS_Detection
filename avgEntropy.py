import fwdPktEntropy
import bckPktEntropy
import fwdBytesEntropy
import bckBytesEntropy
import csvReader
import datetime
import csv
from datetime import timedelta

avgVec = []
for c in range(0,len(fwdPktEntropy.totalPacketsFwdEntropyVec)):
    avgEntropy = (fwdPktEntropy.totalPacketsFwdEntropyVec[c] + bckPktEntropy.totalPacketsBckEntropyVec[c]
                  + fwdBytesEntropy.totalBytesFwdEntropyVec[c] + bckBytesEntropy.totalBytesBckEntropyVec[c])/4
    avgVec.append(avgEntropy)

print(avgVec)
print(len(avgVec))
### ----- End Duration Vector ----- ###

### ----- Time Series Analisys ----- ###
