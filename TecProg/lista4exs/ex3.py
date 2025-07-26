def conferirMaiorItemWhile(lista):
    inicio=0
    final=len(lista)-1
    while inicio!=final:
        if lista[inicio]<lista[final]:
            inicio+=1
        else:
            final-=1
    print(f"O maior valor é {lista[inicio]},na posição {inicio+1}")


conferirMaiorItemWhile(lista=[6,30,9,49,8])


def conferirMaiorItemFor(lista):
    maior=lista[0]
    posicao=0
    for numero in range(len(lista)):
        if lista[numero]>maior:
            maior=lista[numero]
            posicao=numero
    print(f"O maior número na lista é {maior},e está na posição {posicao+1}")

conferirMaiorItemFor(lista=[6,30,9,39,8])