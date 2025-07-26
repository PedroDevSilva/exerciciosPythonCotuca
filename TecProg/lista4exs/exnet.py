alunos = [
    [1, "Alice", [101, 102]],
    [2, "Bruno", [101]],
    [3, "Carla", [103, 104]]
]

disciplinas = [
    [101, "Matemática", 5],
    [102, "História", 3],
    [103, "Física", 4],
    [104, "Biologia", 3]
]
'''
def quantidadeDeDisciplinas(alunos, nomeAluno):#versao com while
    # retorna a quantidade de disciplinas de um aluno específico
    resposta=[]
    i=0
    while i <len(alunos):
        if nomeAluno==alunos[i][1]:
            resposta.extend(alunos[i][2])
            break
        i+=1
    quantidade=len(resposta)
    return quantidade
    ...
print(quantidadeDeDisciplinas(alunos,'Carla'))
'''
'''
def quantidadeDeDisciplinas(alunos,nomeAluno):#versao com for i in (range(len(alunos)))
    resposta=[]
    for i in range(len(alunos)):
        if nomeAluno==alunos[i][1]:
            resposta.extend(alunos[i][2])
            break
    quantidade=len(resposta)
    return quantidade

print(quantidadeDeDisciplinas(alunos,'Carla'))
'''
'''
def quantidadeDeDisciplinas(alunos,nomeAluno):#versao com for
    resposta=[]
    for i in alunos:
        if nomeAluno==i[1]:
            resposta.extend(i[2])
    quantidade=len(resposta)
    return quantidade

print(quantidadeDeDisciplinas(alunos,'Bruno'))
'''



'''
def cargaHorariaDasDisciplinas(alunos, disciplinas, nomeAluno):#versao com while
    # retorna uma lista com as cargas horárias das disciplinas cursadas pelo aluno
    resposta=[]
    i=0
    while i <len(alunos):
        if nomeAluno==alunos[i][1]:
            listaDisciplina=alunos[i][2]
            break
        i+=1
    j=0
    while j <len(disciplinas):
        k=0
        while k<len(listaDisciplina):
            if listaDisciplina[k]==disciplinas[j][0]:
                resposta.append(disciplinas[j][2])
            k+=1
        j+=1
    return resposta

print(cargaHorariaDasDisciplinas(alunos,disciplinas,'Carla'))
'''
'''
def cargaHorariaDasDisciplinas(alunos,disciplinas,nomeAluno):#versao com for i in range(len())
    resposta=[]
    for i in range(len(alunos)):
        if nomeAluno==alunos[i][1]:
            listaDisciplinas=alunos[i][2]
            break
    
    for j in range(len(disciplinas)):
        for k in range(len(listaDisciplinas)):
            if listaDisciplinas[k]==disciplinas[j][0]:
                resposta.append(disciplinas[j][2])
    return resposta

print(cargaHorariaDasDisciplinas(alunos,disciplinas,'Alice'))
'''

def cargaHorariaDasDisciplinas(alunos,disciplinas,nomeAluno):#versao com for, com a variavel sendo o proprio indice
    resposta=[]
    for i in alunos:
        if nomeAluno==i[1]:
            listaDisciplinas=i[2]
            break
    for j in disciplinas:
        for k in listaDisciplinas:
            if k==j[0]:
                resposta.append(j[2])
    return resposta


print(cargaHorariaDasDisciplinas(alunos,disciplinas,'Alice'))