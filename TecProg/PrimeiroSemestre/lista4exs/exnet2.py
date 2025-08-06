produtos = [
    [201, "Camisa", [1, 3]],
    [202, "Calça", [2]],
    [203, "Tênis", [1, 2, 3]]
]

lojas = [
    [1, "Loja A", 59.90],
    [2, "Loja B", 89.99],
    [3, "Loja C", 75.50]
]
'''
def quantidadeDeLojas(produtos, nomeProduto):#versao com while
    # retorna quantas lojas vendem determinado produto
    resposta=[]
    i=0
    while i <len(produtos):
        if nomeProduto==produtos[i][1]:
            resposta.extend(produtos[i][2])
        i+=1
    quantidade=len(resposta)
    return quantidade

print(quantidadeDeLojas(produtos,'Tênis'))
'''
'''
def quantidadeDeLojas(produtos,nomeProduto):#versao com for range
    resposta=[]
    for i in range(len(produtos)):
        if nomeProduto==produtos[i][1]:
            resposta.extend(produtos[i][2])
    quantidade=len(resposta)
    return quantidade

print(quantidadeDeLojas(produtos,'Tênis'))
'''
'''
def quantidadeDeLojas(produtos,nomeProduto):#versao com for
    resposta=[]
    for i in produtos:
        if nomeProduto==i[1]:
            resposta.extend(i[2])
    quantidade=len(resposta)
    return quantidade

print(quantidadeDeLojas(produtos,'Camisa'))
'''
'''
def precosDoProduto(produtos, lojas, nomeProduto):#versao com while
    # retorna lista com os preços do produto nas lojas disponíveis
    resposta=[]
    i=0
    while i <len(produtos):
        if nomeProduto == produtos[i][1]:
            listaLojas=produtos[i][2]
            break
        i+=1
    j=0
    while j<len(lojas):
        k=0
        while k<len(listaLojas):
            if listaLojas[k]==lojas[j][0]:
                resposta.append(lojas[j][2])
            k+=1
        j+=1
    return resposta

print(precosDoProduto(produtos,lojas,'Camisa'))    
'''
'''
def precosDoProduto(produtos,lojas,nomeProduto):#versa com for range
    resposta=[]
    for i in range(len(produtos)):
        if nomeProduto==produtos[i][1]:
            listaLojas=produtos[i][2]
            break
    for j in range(len(lojas)):
        for k in range(len(listaLojas)):
            if listaLojas[k]==lojas[j][0]:
                resposta.append(lojas[j][2])
    return resposta

print(precosDoProduto(produtos,lojas,'Camisa'))
'''

def precosDoProduto(produtos,lojas,nomeProduto):#versao com for
    resposta=[]
    for i in produtos:
        if nomeProduto==i[1]:
            listaLojas=i[2]
            break
    for j in lojas:
        for k in listaLojas:
            if k==j[0]:
                resposta.append(j[2])
    return resposta

print(precosDoProduto(produtos,lojas,'Tênis'))
