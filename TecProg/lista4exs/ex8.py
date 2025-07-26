def posicaoAEsquerdaWhile(lista,numeroDigitado):
    #acharNumero
    i=0
    while i<len(lista):
        if numeroDigitado == lista[i]:
            break
        i+=1
    return lista[i-1]

lista=[5,2,8,4,9,6]
print(posicaoAEsquerdaWhile(lista,2))

def posicaoAEsquerdaFor(lista,numeroDigitado):
    for i in range(len(lista)):
        if numeroDigitado == lista[i]:
            break
    return lista[i-1]

lista=[5,2,8,4,9,6]
print(posicaoAEsquerdaFor(lista,2))