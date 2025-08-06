
def conferirMenorItemWhile(lista):
    inicio=0
    final=len(lista)-1
    while inicio!=final:
        if lista[inicio]>lista[final]:
            inicio+=1
        else:
            final-=1
    print(f"O menor item é {lista[final]}, e está na posicão {final+1}")

conferirMenorItemWhile(lista=[1,6,4,76,65,12])


def conferirMenorItemFor(lista):
    menor=lista[0]
    posicao=0
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
            posicao=i
    print(f"O menor item é {menor}, e está na posicão {posicao+1}")
        
conferirMenorItemFor(lista=[10,6,4,76,65,12])