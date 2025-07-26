def contadorNumeroWhile(lista,numeroDigitado):
    i=0
    contador=0
    while i<len(lista):
        if numeroDigitado == lista[i]:
            contador+=1
        i+=1
    return contador

lista=[1,2,3,5,5,5,6,7,8,5]
print(contadorNumeroWhile(lista,5))

def contadorNumeroFor(lista,numeroDigitado):
    contador=0
    for i in range(len(lista)):
        if numeroDigitado == lista[i]:
            contador+=1
    return contador

lista=[1,2,3,5,5,5,6,7,8]
print(contadorNumeroFor(lista,5))