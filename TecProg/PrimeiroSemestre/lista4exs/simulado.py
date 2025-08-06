produtos=[
    [101, "Café em pó", [1, 3]],
    [102, "Açúcar cristal", [2]],
    [103, "Leite em pó", [1, 2]],
    [104, "Achocolatado", [3, 4]]
]

fornecedor=[
    [1, "Alimentos Brasil", "São Paulo"],
    [2, "Doces do Vale", "Minas Gerais"],
    [3, "Delícias do Sul", "Rio Grande do Sul"],
    [4, "NutriCenter", "Paraná"]
]

#1.
def fornecedorProduto(produtos,nomeProduto):
    resposta=[]
    for i in range(len(produtos)):
        if nomeProduto == produtos[i][1]:
            idFornecedor=produtos[i][2]
            break
    for j in range(len(idFornecedor)):
        for k in range(len(fornecedor)):
            if idFornecedor[j]== fornecedor[k][0]:
                resposta.append(fornecedor[k][1])
    return resposta

print(fornecedorProduto(produtos,'Leite em pó'))

#2.
def quantasPalavrasComLetraInicial(frase,letra):
    novaFrase=frase.lower()
    contador=0
    i=0
    while i<len(novaFrase):
        if letra==novaFrase[i]:
            if novaFrase[i-1] == ' ' or novaFrase[i]==novaFrase[0]:
                contador+=1
        i+=1
    return contador

print(quantasPalavrasComLetraInicial('O rato Roeu a Roupa do rei de Roma','r'))
print(quantasPalavrasComLetraInicial('Maria mora no mato','m'))