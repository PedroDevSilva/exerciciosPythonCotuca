def confirmarElementosParesWhile(lista):
    i=0
    while i <len(lista):
        if lista[i] % 2 == 0:
            return True
        else:
            return False
        i+=1

print(confirmarElementosParesWhile(lista=[2,2,2]))

def confirmarElementosParesFor(lista):
    for i in lista:
        if i % 2 == 0:
            return True
        else:
            return False
        
print(confirmarElementosParesFor(lista=[1,2,2]))