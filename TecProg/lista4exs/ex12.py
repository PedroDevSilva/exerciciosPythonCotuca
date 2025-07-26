def numeroADireitaWhile(lista1,lista2):
    i=0
    j=0
    while i < len(lista2):
        if lista2[i] in lista1:
            while j < len(lista1):
                if lista2[i]==lista1[j]:
                    return lista1[j+1]
                    break
                j+=1
        i+=1

lista1=[1,3,5,7,9]
lista2=[2,4,3]

print(numeroADireitaWhile(lista1,lista2))

def numeroADireitaFor(lista1,lista2):
    for i in range(len(lista2)):
        if lista2[i] in lista1:
            for j in range(len(lista1)):
                if lista2[i]==lista1[j]:
                    return lista1[j+1]
                    break
lista1=[1,3,5,7,9]
lista2=[2,4,5]

print(numeroADireitaFor(lista1,lista2))