def mediaNumerosWhile(lista):
    i=0
    soma=0
    while i<len(lista):
        soma+=lista[i]
        i+=1
    media=soma/len(lista)
    print(media)

mediaNumerosWhile(lista=[10,0,10,10,10])

def mediaNumerosFor(lista2):
    soma=0
    for i in lista2:
        soma+=i
    media=soma/len(lista2)
    print(media)

mediaNumerosFor(lista2=[8,8,8,0])