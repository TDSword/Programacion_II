
# primero las funciones

def ks(k):
    if k == 2:
        print("k!")
        k += 1
    elif k == 3:
        print('k?')
    else:
        print('k...')



def knt(k):
    k += 1
    return k

# Segundamente definimos
k = 1

# Posteriormente aplicando Gauss podemos llegar a la tan esperada escalera de Rufinni
ks(knt(k))
ks(knt(knt(k)))
ks(knt(knt(knt(k))))
