def posicaoADireitaWhile(lista,numeroDigitado):
    i=0
    while i<len(lista):
        if numeroDigitado==lista[i]:
            break
        i+=1
    return lista[i+1]

lista=[2,5,1,8,3,9]
print(posicaoADireitaWhile(lista,3))

def posicaoADireitaFor(lista,numeroDigitado):
    for i in range(len(lista)):
        if numeroDigitado==lista[i]:
            break
    return lista[i+1]

lista=[2,5,1,8,3,9]
print(posicaoADireitaFor(lista,2))