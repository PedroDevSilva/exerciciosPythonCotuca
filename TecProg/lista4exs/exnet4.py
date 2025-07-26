livros = [
    [401, "Dom Casmurro", [601, 602, 604]],
    [402, "1984", [601]],
    [403, "O Pequeno Príncipe", [602, 603]]
]

bibliotecas = [
    [601, "Central", "08:00–18:00"],
    [602, "Setorial", "09:00–17:00"],
    [603, "Fatorial", "10:00-19:00"],
    [604, "Infantil", "11:00–16:00"]
]
'''
def bibliotecasComLivro(livros, tituloLivro):#versao com while
    # retorna a quantidade de bibliotecas com o livro
    resposta=[]
    i=0
    while i <len(livros):
        if tituloLivro==livros[i][1]:
            resposta.extend(livros[i][2])
            break
        i+=1
    quantidade=len(resposta)
    return quantidade
'''
'''
def bibliotecasComLivro(livros,tituloLivro):#versao com for range
    resposta=[]
    for i in range(len(livros)):
        if tituloLivro==livros[i][1]:
            resposta.extend(livros[i][2])
            break
    quantidade=len(resposta)
    return quantidade
'''
'''
def bibliotecasComLivro(livros,tituloLivro):# versao com for
    resposta=[]
    for i in livros:
        if tituloLivro==i[1]:
            resposta.extend(i[2])
            break
    quantidade=len(resposta)
    return quantidade

print(bibliotecasComLivro(livros,'1984'))
'''


'''
def horariosDeFuncionamento(livros, bibliotecas, tituloLivro):#versao com while
    # retorna lista com os horários das bibliotecas que têm o livro
    resposta=[]
    i=0
    while i <len(livros):
        if tituloLivro==livros[i][1]:
            listaBiblioteca=livros[i][2]
            break
        i+=1
    
    j=0
    while j <len(bibliotecas):
        k=0
        while k <len(listaBiblioteca):
            if listaBiblioteca[k]==bibliotecas[j][0]:
                resposta.append(bibliotecas[j][2])
            k+=1
        j+=1
    return resposta
'''

def horariosDeFuncionamento(livros,bibliotecas,tituloLivro):#versao com for range
    resposta=[]
    for i in range(len(livros)):
        if tituloLivro==livros[i][1]:
            listaBiblioteca=livros[i][2]
            break
    for j in range(len(bibliotecas)):
        for k in range(len(listaBiblioteca)):
            if listaBiblioteca[k]==bibliotecas[j][0]:
                resposta.append(bibliotecas[j][2])
    return resposta

'''
def horariosDeFuncionamento(livros,bibliotecas,tituloLivro):#versao com for
    resposta=[]
    for i in livros:
        if tituloLivro==i[1]:
            listaBiblioteca=i[2]
            break
    for j in bibliotecas:
        for k in listaBiblioteca:
            if k == j[0]:
                resposta.append(j[2])
    return resposta
'''
print(horariosDeFuncionamento(livros,bibliotecas,"Dom Casmurro"))