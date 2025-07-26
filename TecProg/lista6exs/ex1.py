def cadeia():
    texto=str(input("Digite seu texto com comandos python e os retornarei com os comandos aplicados: "))
    resultado=""
    indice=0
    while indice < len(texto):
        if texto[indice] == '\\' and indice + 1 < len(texto):
            if texto[indice+1] in ['n', 't', 'a', 'b', 'f', 'r', 'v', '\\', '\'']:
                texto[indice].split('')
        indice+=1
    print(f"seu texto com comandos fica: {texto}")
    

    

cadeia()