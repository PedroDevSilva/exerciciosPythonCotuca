def numeroAEsquerdaSequenciaWhile(sequencia, listaMaior):#versao com while
    i = 0
    while i <= len(listaMaior) - len(sequencia):
        j = 0
        confirmarSequencia = []
        while j < len(sequencia):
            confirmarSequencia.append(listaMaior[i + j])
            j += 1
        if confirmarSequencia == sequencia:
            return i
        i += 1
    return -1

# Teste
sequencia = [3, 5, 7]
listaMaior = [1, 2, 3, 5, 7, 9]
print(numeroAEsquerdaSequenciaWhile(sequencia, listaMaior))


def numeroAEsquerdaSequenciaFor(sequencia, listaMaior):#versao com for range
    for i in range(len(listaMaior)-len(sequencia)+1):
        confirmarSequencia=[]
        for k in range(len(sequencia)):
            confirmarSequencia.append(listaMaior[i+k])
        if confirmarSequencia==sequencia:
            return listaMaior[i-1]
    return -1
                

# Teste
sequencia = [3, 4]
listaMaior = [1, 2, 3, 4, 5]
print(numeroAEsquerdaSequenciaFor(sequencia, listaMaior))

