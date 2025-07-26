import os
os.system('cls')
#tipo2

'''livros=
[
 [idLivro,nomeLivro,listaIdAutor]
 ...
]

autores=
[
 [idAutor,nomeAutor,anoNascimentoAutor]
 ...
]
'''

livros = [
    [1, "Dom Casmurro", [1]],
    [2, "O Cortiço", [2]],
    [3, "Memórias Póstumas de Brás Cubas", [1]],
    [4, "Capitães da Areia", [3]],
    [5, "A Hora da Estrela", [4]],
    [6, "Grande Sertão: Veredas", [5]],
    [7, "Livro com Vários Autores", [1, 2, 4]]  # exemplo com múltiplos autores
]
autores = [
    [1, "Machado de Assis", 1839],
    [2, "Aluísio Azevedo", 1857],
    [3, "Jorge Amado", 1912],
    [4, "Clarice Lispector", 1920],
    [5, "João Guimarães Rosa", 1908]
]
'''retornar lista com livros do autor
def LivrosDoAutor (livros,idAutor):
    resposta=[]
    posicao=0
    while posicao<len(livros):
        if idAutor in livros[posicao][2]:
            resposta.append(livros[posicao][1])
        posicao+=1
    return resposta

idAutor=2
livros_encontrados=LivrosDoAutor(livros,idAutor)
print(livros_encontrados,len(livros_encontrados))
'''

'''
def LivrosDoAutor(livros,idAutor): #usando o for na lista de livros, o proprio for se torna o indice, por isso nao é necessário escrever 'livros[posicao][2]'
    resposta=[]
    for livro in livros:
        if idAutor in livro[2]:
            resposta.append(livro[1])
    return resposta

print(LivrosDoAutor(livros,1))
'''
'''
def LivrosDoAutor(livros,idAutor): #usando o for com range, precisamos identificar a posicao, no caso livros[livro[2]]
    resposta=[]
    for livro in range(len(livros)):
        if idAutor in livros[livro][2]:
            resposta.append(livros[livro][1])
    return resposta

idAutor=1
livrosEcontrados=LivrosDoAutor(livros,idAutor)
print(livrosEcontrados,len(livrosEcontrados))
'''


#retornar lista com os anos de nascimento dos autores do livro, cujo titulo fornecido

def anosDosAutores(livros,autores,nomeLivro):
    resposta=[]
    listaDeAutores=[]
    for livro in livros:
        if nomeLivro == livro[1]:
            listaDeAutores=livro[2]
            break

    for autor in autores:
        if autor[0] in listaDeAutores:
            resposta.append(2025-autor[2])
            print(autor[1])
    return resposta
        

nomeLivro='Livro com Vários Autores'
listaNascimento=anosDosAutores(livros,autores,nomeLivro)
print(listaNascimento)


'''
def anosDosAutores(livros,autores,nomeLivro):
    resposta=[]
    i=0
    while i<len(livros):
        if nomeLivro == livros[i][1]:
            listaDeAutores=livros[i][2]
            break
        i+=1

    j=0
    while j<len(listaDeAutores):
        posicaoA=0
        while posicaoA<len(autores):
            if listaDeAutores[j]==autores[posicaoA][0]:
                resposta.append(2025-autores[posicaoA][2])
                print(autores[posicaoA][1])
            posicaoA+=1
        j+=1
    
    return resposta

nomeLivro='Livro com Vários Autores'
listaNascimento=anosDosAutores(livros,autores,nomeLivro)
print(listaNascimento)
'''
'''
def anosDosAutores(livros,autores,nomeLivro):
    resposta=[]
    listaDeAutores=[]
    for livro in range(len(livros)):
        if nomeLivro in livros[livro][1]:
            listaDeAutores = livros[livro][2]
            break
    
    for i in range(len(listaDeAutores)):
        autorAtual=listaDeAutores[i]
        for j in range(len(autores)):
            if autorAtual == autores[j][0]:
                idade=2025-autores[j][2]
                resposta.append(idade)
                print(autores[j][1])
                break

    return resposta

nomeLivro='Livro com Vários Autores'
listaNascimento=anosDosAutores(livros,autores,nomeLivro)
print(listaNascimento)
'''