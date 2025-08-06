jogadores = [
    [1, "Alice", [301, 302]],
    [2, "Bruno", [302, 303]],
    [3, "Carla", [301, 303]]
]
jogos = [
    [301, "FIFA 23", [501, 502]],
    [302, "Minecraft", [503]],
    [303, "Valorant", [501, 503]]
]
plataformas = [
    [501, "PC", 0],
    [502, "PlayStation", 199.90],
    [503, "Xbox", 179.90]
]
avaliacoes = [
    [1, 301, 9.0],
    [1, 302, 8.5],
    [2, 302, 9.5],
    [2, 303, 7.0],
    [3, 301, 8.0],
    [3, 303, 9.2]
]

'''
def notaJogador(nomeJogador):#versao com while
    resposta=[]
    i=0
    while i<len(jogadores):
        if nomeJogador==jogadores[i][1]:
            idJogador=jogadores[i][0]
            listaJogos=jogadores[i][2]
            break
        i+=1
    
    j=0
    while j<len(jogos):
        k=0
        while k<len(listaJogos):
            if listaJogos[k]==jogos[j][0]:
                resposta.append(jogos[j][1])
                l=0
                while l<len(avaliacoes):
                    if idJogador==avaliacoes[l][0] and jogos[k]==avaliacoes[l][1]:
                        resposta.append(avaliacoes[l][2])
                    l+=1
            k+=1
        j+=1
    return resposta

print(notaJogador("Carla"))
'''

def notaJogador(nomeJogador):
    resposta=[]
    