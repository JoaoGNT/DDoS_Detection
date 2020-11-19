a = [1,2,3,4,5,6]
print(a[0:5])


for t in range(5,15):
   print(t)
   print(t-5)













v = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
b =[]
c=[]
print(type(v[1]))

def lista_simples(lista):
    if isinstance(lista, list):
        return [sub_elem for elem in lista for sub_elem in lista_simples(elem)]
    else:
        return [lista]

for t in range(0,len(v)):
    vec = v[t]

    b.append(lista_simples(vec))
    # for s in range(0,len(vec)):
    #     vec2 = vec[s]
    #
    #     for w in range(0,len(vec2)):
    #         element = vec2[w]
    # a = element
    # b.append(a)
print(b)
print(c)
print(v)