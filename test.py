v = [[19,2,3,4,5,1],[1,2,3,5,5,1],[1,3,4,5,5,1],[1,6,8,9,10,1]]
suma = []
S=[]


for r in range(0,len(v[0])):
    for j in range(0, len(v)):
        suma.append(v[j][r])
    soma = sum(suma)
    suma = []
    S.append(soma)

print(S)
print(v)

l = len(v[0])
contador = 0
for k in range(0,l):

    if S[k] <= 18:

        for j in range(0,len(v)):
            del v[j][k-contador]
        contador = contador + 1

print(v)

ar = []
bt=[]

for rr in range(0,len(v[0])):
    for jj in range(0, len(v)):
        ar.append(v[jj][rr])
    h = sum(ar)
    ar = []
    bt.append(h)
print(bt)
