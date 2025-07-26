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
'''
def ondeEstaDisponivel(jogos, nomeJogo):#versao com while
    # retorna quantidade de plataformas disponíveis para o jogo
    resposta=[]
    i=0
    while i <len(jogos):
        if nomeJogo==jogos[i][1]:
            resposta.extend(jogos[i][2])
            break
        i+=1
    quantidade=len(resposta)
    return quantidade

print(ondeEstaDisponivel(jogos,'Minecraft'))
'''
'''
def ondeEstaDisponivel(jogos,nomeJogo):#versao com for range
    resposta=[]
    for i in range(len(jogos)):
        if nomeJogo==jogos[i][1]:
            resposta.extend(jogos[i][2])
            break
    quantidade=len(resposta)
    return quantidade

print(ondeEstaDisponivel(jogos,'Valorant'))
'''
'''
def ondeEstaDisponivel(jogos,nomeJogo):#versao com for
    resposta=[]
    for i in jogos:
        if nomeJogo==i[1]:
            resposta.extend(i[2])
            break
    quantidade=len(resposta)
    return quantidade

print(ondeEstaDisponivel(jogos,'Valorant'))
'''
'''
def precoNasPlataformas(jogos, plataformas, nomeJogo):#versao com while
    # retorna os preços do jogo nas plataformas disponíveis
    resposta=[]
    i=0
    while i<len(jogos):
        if nomeJogo==jogos[i][1]:
            listaPlataformas=jogos[i][2]
            break
        i+=1
    j=0
    while j<len(plataformas):
        k=0
        while k<len(listaPlataformas):
            if listaPlataformas[k]==plataformas[j][0]:
                resposta.append(plataformas[j][2])
            k+=1
        j+=1
    return resposta

print(precoNasPlataformas(jogos,plataformas,'Valorant'))
'''
'''
def precoNasPlataformas(jogos,plataformas,nomeJogo):#versao com for range
    resposta=[]
    for i in range(len(jogos)):
        if nomeJogo==jogos[i][1]:
            listaPlataformas=jogos[i][2]
            break
    for j in range(len(plataformas)):
        for k in range(len(listaPlataformas)):
            if listaPlataformas[k]==plataformas[j][0]:
                resposta.append(plataformas[j][2])
    return resposta

print(precoNasPlataformas(jogos,plataformas,'Valorant'))
'''

def precoNasPlataformas(jogos,plataformas,nomeJogo):#versao com for
    resposta=[]
    for i in jogos:
        if nomeJogo==i[1]:
            listaPlataformas=i[2]
            break
    for j in plataformas:
        for k in listaPlataformas:
            if k==j[0]:
                resposta.append(j[2])
    return resposta

print(precoNasPlataformas(jogos,plataformas,'Minecraft'))