import os
import pyodbc

def menu():
    os.system('cls')
    print ('\n\n\t*** C A D A S T R O   D E   A U T O R E S ***\n\n')
    print ('\t1. Listar Autores')
    print ('\t2. Incluir Novo Autor')
    print ('\t3. Alterar Autor Existente')
    print ('\t4. Excluir Autor Existente')
    print ('\t5. Pesquisar por Autor')
    print ('\n\t0. SAIR\n\n')

def mensagem(msg):
    print ('\n\t*********************')
    print ('\t'+msg)
    print ('\t*********************')
    pausa('Tecle <ENTER> para continuar ....')

def qualOpcao():
    while (True):
        op = int(input ('\tEscolha uma opção:'))
        if (op>=0) and (op<6):
            return op
        mensagem('Opção INVALIDA, tente outro valor ...')
    
def listar():
    conn = conectar(SERVER_NAME, DATABASE, USER, PASSWORD)
    cursor = conn.cursor()
    # Executando uma consulta
    cursor.execute("SELECT * FROM ct_autor")

    os.system('cls')
    print('\tId\tNome')
    print('\t---------------------------------')
    for row in cursor.fetchall():
        print('\t'+str(row[0])+'\t'+row[1])
    print('\t---------------------------------')
    cursor.close()
    conn.close
    pausa('Tecle <ENTER> para continuar ....')

def incluir():
    os.system('cls')
    print ('\n\n\t*** INCLUSÃO DE AUTOR ***\n\n')
    nome = input('\tNome: ')
    sql = f"INSERT INTO ct_autor (nome) VALUES ('{nome}')"
    executaSQL(sql)
    mensagem('Autor incluido com sucesso!')

def alterar():
    os.system('cls')
    print ('\n\n\t*** ALTERAÇÃO DE AUTOR ***\n\n')
    id = int(input('\tId do Autor: ')) # Converter o id lido para numero
    nome = input('\n\tNovo Nome: ')
    sql = f"UPDATE ct_autor SET nome='{nome}' WHERE id={id}"
    executaSQL(sql)
    mensagem('Autor alterado com sucesso!')

def executaSQL(sql):
    conn = conectar(SERVER_NAME, DATABASE, USER, PASSWORD)
    cursor = conn.cursor()   
    cursor.execute(sql)    
    cursor.commit()
    cursor.close()
    conn.close()

def excluir():
    os.system('cls')
    print ('\n\n\t*** ALTERAÇÃO DE AUTOR ***\n\n')
    id=int(input("Digite o ID do autor a ser excluido: "))
    sql=f'DELETE FROM ct_AUTOR WHERE id={id}'
    executaSQL(sql)
    mensagem('AUTOR EXCLUIDO COM SUCESSO')


def pesquisar():
    os.system('cls')
    print('\n\n\t*** PESQUISA DE AUTOR ***\n\n')
    pesquisa = input("Digite o nome (ou parte) do Autor a ser pesquisado: ")

    conn = conectar(SERVER_NAME, DATABASE, USER, PASSWORD)
    cursor = conn.cursor()

    sql = f"SELECT id, nome FROM ct_autor WHERE nome LIKE ?"
    cursor.execute(sql, ('%' + pesquisa + '%',))

    print('\n\tId\tNome')
    print('\t--------------------------')
    for row in cursor.fetchall():
        print(f'\t{row[0]}\t{row[1]}')
    print('\t--------------------------')

    cursor.close()
    conn.close()
    pausa('Tecle <ENTER> para continuar ....')


def pausa(msg):
    msg = '\t'+msg
    input(msg)

# ************************************** METODOS PARA O BANCO ***
def conectar(server, database, username, password):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    return conn    
# ************************************** CONSTANTES DE BANCO
SERVER_NAME = 'regulus.cotuca.unicamp.br'
USER = 'BD25529'
PASSWORD = 'BD25529'
DATABASE = 'BD25529'
# ************************************** INICIO DO PROGRAMA ***
while (True):
    menu()
    opcao = qualOpcao() # solicita e valida
    
    match opcao: 
        case 0: 
            break
        case 1: 
            # Executando uma consulta
            listar()
        case 2: 
            incluir()
        case 3: 
            alterar()
        case 4: 
            excluir()
        case 5:
            pesquisar()
