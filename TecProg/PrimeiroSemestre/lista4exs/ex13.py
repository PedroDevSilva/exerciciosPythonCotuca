def contadorDuasListasWhile(lista1,lista2):
    i=0
    contador=0
    while i<len(lista1):
        if lista1[i] in lista2:
            j=0
            while j <len(lista2):
                if lista1[i]==lista2[j]:
                    contador+=1
                j+=1
        i+=1
    return contador

lista1=[1,7,3,5]
lista2=[1,2,3,3,4,5,5]
print(contadorDuasListasWhile(lista1,lista2))

def contadorDuasListasFor(lista1,lista2):
    contador=0
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            for j in range(len(lista2)):
                if lista1[i]==lista2[j]:
                    contador+=1
                    j=0
    return contador

lista1=[1,7,3,5]
lista2=[1,2,3,3]
print(contadorDuasListasFor(lista1,lista2))