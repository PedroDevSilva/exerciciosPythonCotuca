def somarItensListaWhile(lista):
    total=0
    i=0
    while i<len(lista):
        total+=lista[i]
        i+=1
    print(total)

somarItensListaWhile(lista=[10,5,5])


def somarItensListaFor(lista2):
    total=0
    for i in lista2:
        total+=1
    print(total)

somarItensListaFor(lista2=[10,20,20])
