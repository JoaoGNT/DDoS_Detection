import fwdPktEntropy
import bckPktEntropy
import fwdBytesEntropy
import bckBytesEntropy

# print(fwdPktEntropy.totalPacketsFwdEntropyVec[0:15])
# print(bckPktEntropy.totalPacketsBckEntropyVec[0:15])
# print(fwdBytesEntropy.totalBytesFwdEntropyVec[0:15])
# print(bckBytesEntropy.totalBytesBckEntropyVec[0:15])
#
# print(len(fwdPktEntropy.totalPacketsFwdEntropyVec))
# print(len(bckPktEntropy.totalPacketsBckEntropyVec))
# print(len(fwdBytesEntropy.totalBytesFwdEntropyVec))
# print(len(bckBytesEntropy.totalBytesBckEntropyVec))

avgVec = []

for c in range(0,len(fwdPktEntropy.totalPacketsFwdEntropyVec)):
    avgEntropy = (fwdPktEntropy.totalPacketsFwdEntropyVec[c] + bckPktEntropy.totalPacketsBckEntropyVec[c]
                  + fwdBytesEntropy.totalBytesFwdEntropyVec[c] + bckBytesEntropy.totalBytesBckEntropyVec[c])/4
    avgVec.append(avgEntropy)


