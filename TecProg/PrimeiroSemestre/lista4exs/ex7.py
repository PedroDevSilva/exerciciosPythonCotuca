def conferirListaCrescenteWhile(lista):
    i=0
    while i<len(lista)-1:
        if lista[i]>lista[i+1]:
            return False
        i+=1
    return True

print(conferirListaCrescenteWhile(lista=[5,2,3]))

def conferirListaCrescenteFor(lista):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            return False
    return True

print(conferirListaCrescenteFor(lista=[1,2,3,4]))
