import os
os.system('cls')

def quantosNumerosAbaixoDaMediaWhile(lista):
    resposta=[]
    total=0
    posicao=0
    while posicao<len(lista):
        total+=lista[posicao]
        posicao+=1
    media=total/len(lista)
    i=0
    while i<len(lista):
        if lista[i]<media:
            resposta.append(lista[i])
        i+=1
    return resposta

print(quantosNumerosAbaixoDaMediaWhile(lista=[10,10,10,2,1]))


def quantosNumerosAbaixoDaMediaFor(lista):
    resposta=[]
    total=0
    for numero in lista:
        total+=numero
    media=total/len(lista)
    for i in lista:
        if i<media:
            resposta.append(i)
    return resposta

print(quantosNumerosAbaixoDaMediaFor(lista=[10,10,2,1]))