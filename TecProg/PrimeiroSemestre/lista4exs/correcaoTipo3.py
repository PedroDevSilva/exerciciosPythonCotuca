import os
os.system('cls')
'''
FILMES:
[
 [idDoFilme,tituloDoFilme,listaDasPlataformasOndeEstáDisponivel]
 ...
]

PLATAFORMAS:
[
 [idDaPlataforma,nomeDaPlataforma,valorEmReaisDaAssinaturaPorMes]
 ...
]'''

FILMES = [
    [1, "O Poderoso Chefão", [1, 3]],
    [2, "Interestelar", [2]],
    [3, "Parasita", [1, 2, 4]],
    [4, "Matrix", [2, 4]],
    [5, "Cidade de Deus", [1, 5]],
    [6, "Clube da Luta", [3]],
    [7, "La La Land", [4, 5]],
    [8, "O Irlandês", [1, 2]],
    [9, "Corra!", [2, 3]],
    [10, "Whiplash", [3, 4]]
]
PLATAFORMAS = [
    [1, "Netflix", 39.90],
    [2, "Amazon Prime Video", 19.90],
    [3, "HBO Max", 34.90],
    [4, "Disney+", 27.90],
    [5, "Globoplay", 24.90]
]
'''
def quantidadeDePlataformas(filmes,tituloFilme):
    resposta=[]
    i=0
    while i < len(filmes):
        if tituloFilme in filmes[i][1]:
            plataforma=filmes[i][2]
            resposta.extend(plataforma)
        i+=1
    numero=len(resposta)
    return f'Está disponível em {numero} plataformas! cujo id é {resposta}'

print(quantidadeDePlataformas(FILMES,'O Poderoso Chefão'))
'''
'''
def quantidadeDePlataforma(filmes,nomeFilme):
    resposta=[]
    for filme in filmes:
        if nomeFilme in filme[1]:
            plataforma=filme[2]
            resposta.extend(plataforma)
    numero=len(resposta)
    return f'Está disponível em {numero} plataformas! cujo id é {resposta}'

print(quantidadeDePlataforma(FILMES,'O Poderoso Chefão'))
'''
'''
def quantidadeDePlataforma(filmes,nomeFilme):
    resposta=[]
    for filme in range(len(filmes)):
        if nomeFilme in filmes[filme][1]:
            plataforma=filmes[filme][2]
            resposta.extend(plataforma)
    numero=len(resposta)
    
    return f'Está disponível em {numero} plataformas! cujo id é {resposta}'

print(quantidadeDePlataforma(FILMES,'O Poderoso Chefão'))
'''
'''
def valoresPlataformas(filmes,plataformas,tituloFilme):
    resposta=[]
    i=0
    while i <len(filmes):
        if tituloFilme == filmes[i][1]:
            listaPlataformas=filmes[i][2]
            break
        i+=1
    j=0
    while j<len(listaPlataformas):
        k=0
        while k <len(plataformas):
            if listaPlataformas[j]==plataformas[k][0]:
                resposta.append(plataformas[k][2])
                print(plataformas[k][1])
                break
            k+=1
        j+=1
    return resposta

print(valoresPlataformas(FILMES,PLATAFORMAS,'Matrix'))
'''
'''
def valoresPlataformas(filmes,plataformas,tituloFilme):
    resposta=[]
    for filme in filmes:
        if tituloFilme==filme[1]:
            listaPlataformas=filme[2]
            break

    for j in plataformas:
        for k in listaPlataformas:
            if k == j[0]:
                resposta.append(j[2])
    return resposta

print(valoresPlataformas(FILMES,PLATAFORMAS,'Cidade de Deus'))
'''

def valoresPlataformas(filmes,plataformas,tituloFilme):
    resposta=[]
    for i in range(len(filmes)):
        if tituloFilme==filmes[i][1]:
            listaPlataformas=filmes[i][2]
            break
    for j in range(len(plataformas)):
        for k in range(len(listaPlataformas)):
            if listaPlataformas[k]==plataformas[j][0]:
                resposta.append(plataformas[j][2])
    return resposta


print(valoresPlataformas(FILMES,PLATAFORMAS,'Matrix'))