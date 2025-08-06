import pyodbc


def conectar(server, database, username, password):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    return conn


def exibir_dados(cursor):
    # Recuperando os resultados
    for row in cursor.fetchall():
        print(row)


##### INICIO DO PROGRAMA        

# Conectando ao banco de dados
conn = conectar('regulus.cotuca.unicamp.br', 'BD25529', 'BD25529', 'BD25529')
cursor = conn.cursor()


tabela=input("Digite o nome da tabela que deseja conferir os dados cadastrados: ")
# Executando uma consulta
cursor.execute(f"SELECT * FROM {tabela}")
exibir_dados(cursor)

# Fechando a conexão
cursor.close()
conn.close()