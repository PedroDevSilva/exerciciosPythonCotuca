
'''
#STRINGS:

print("tuc" in "cotuca")#a funcao in retorna true ou false se o primeiro termo existir ou não no segundo termo

print("cotuca".find("tuc")) #retorna a posição do parâmetro entre o parênteses

texto="Programar é preciso, viver não é preciso!"

lista=texto.split()#split utiliza como parâmetro digitado entre os parênteses para separar a frase em "pedaços"
print(lista)

escola="COTUCA"
texto2=escola.replace("C","K")#replace troca todos os primeiros termos digitado pelo segundo em um texto
print(texto2)

lista2=list(texto2)#forma uma lista com todos os caracteres em uma string/frase
print(lista2)

novotexto="".join(lista2)#join junta os itens de uma lista usando o nome da lista como parâmetro
print(novotexto)
'''
'''
#TUPLAS:#São como listas porém, imutáveis. Identificadas por meio de parênteses

tupla=(2,3,5,7,9,11,13,15,17)
print(tupla)

print(tupla[2::2])

tuplavazia=()
print(tuplavazia)

tupla1elemento=(2,)
print(tupla1elemento)

print(len(tupla1elemento))

novatupla=tupla+(19,21,23)
print(novatupla)

print(11 in novatupla)#possível usar in com tuplas
'''
'''
#DICIONÁRIOS:#Escritos entre chaves
#Estrutura de dados que mapeia chave à um valor
#Funciona como índice para acessar uma chave

#String a qual associei (com ":") alguma outra característica ("nota")
nota={"Ana":10,"Pedro":7.5,"José":4,"João":5.5}
print(nota["José"])

#DICIONÁRIO NÃO É ORDENÁVEL
'''
'''
#Abaixo temos a impressão de que existem duas listas, atribuindo a outra lista à lista
#Porém, isso é apenas uma lista com dois nomes diferentes
lista=[2,4,6,8]
outralista=lista
print(lista)
print(outralista)
lista.append(10)
print(lista)
print(outralista)
#Podemos confirmar isto usando a função id
print(id(lista))
print(id(outralista))
#Para copiarmos uma lista e criar uma nova, usamos a função copy. Assim atribuindo outro espaço na memória do pc
novalista=lista.copy()
novalista.append(90)
print(novalista)
'''

'''
ShallowCopy and DeepCopy:
Utilizando o .copy() em uma situação aonde existem listas dentro de listas, ele faz o que nomeamos como cópia raza. 
Apesar da lista maior ter outro id, elas continuam referenciando a mesma.
Se precisarmos alterar apenas um item de uma lista menor, alterará em ambas as listas, pois ambas se referenciam.
Nesse caso, podemos alterar a lista menor inteira, de tal modo a cópia não interferirá na original e vice versa.
'''
'''
#Podemos importar o copy e usar o comando copy.deepcopy() para fazer um deep copy seguro e eficiente, também é possível programar um
import copy
lista=[[2,3,4],[5,6,7]]
deepcopylista=copy.deepcopy(lista)
deepcopylista[0][0]=99
print(lista)
print(deepcopylista)
'''
'''
#Dict transforma lista ou tupla em dicionário
tupla=(("Jõao",30),("Maria",27))
dicionario=dict(tupla)
print(dicionario)
'''
'''
tupla=(("Jõao",30),("Maria",27))
dicionario=dict(tupla)
novodicionario=dicionario.fromkeys(["João","Maria"],[15,20])
print(novodicionario)
print(novodicionario.get("João"))

print(novodicionario.items())#retorna todos os itens do dicionario
print(novodicionario.keys())#retorna só as chaves
print(novodicionario.values())#retorna só os valores
'''
'''
dicio={"Julia":19,"Rogério":22}
outrodicio={"Clebinho":21,"Rogério":23}
dicio.update(outrodicio)#Update podendo fundir dicionário e atualizando-os
print(dicio)
idade=dicio.pop("Clebinho")#remove os pares de chv/valor e retorna podendo guardar em uma variável o valor
print(dicio)
print(idade)
ret=dicio.popitem()#remove ultimo tem e guarda na variavel chv/valor como tupla
print(dicio)
print(ret)
'''
'''
#Podemos usar o for dentro de uma atribuição de um dicionário, atualizando, neste caso adicionando um 9 para cada valor contido em cada chave
#Devemos atribuir o número como str antes para não dar erro por tentar concatenar int com str do loop
contatos={"Pedro":'94335851',"João":'23723732',"Roberta":'82363833'}
print(contatos)
contatos={nome:'9'+contatos[nome] for nome in contatos}
print(contatos)
'''
#Caracterizando conteúdo
#Usando loop com for, podemos definir lugares usando uma regra de formação, por exemplo:
lista=[0 for i in range(10)]
print(lista)
