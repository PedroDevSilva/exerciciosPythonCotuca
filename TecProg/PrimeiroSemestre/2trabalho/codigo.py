def ler_matriz(nome_arquivo):
    matriz = []
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            numeros = linha.strip().split()
            matriz.append([float(n) for n in numeros])
    return matriz

def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)
    print()

def trocar_linhas(matriz, indice_linha_1, indice_linha_2):
    matriz[indice_linha_1], matriz[indice_linha_2] = matriz[indice_linha_2], matriz[indice_linha_1]

def poe1numaLinhaDaRegiaoPreta(indice_linha, mat):
    divisor = mat[indice_linha][indice_linha]
    for indice_coluna in range(len(mat[0])):
        mat[indice_linha][indice_coluna] /= divisor

def metodo_gauss(matriz):
    total_linhas = len(matriz)

    for indice_pivo in range(total_linhas):
        if matriz[indice_pivo][indice_pivo] == 0:
            trocou = False
            for linha_busca in range(indice_pivo + 1, total_linhas):
                if matriz[linha_busca][indice_pivo] != 0:
                    trocar_linhas(matriz, indice_pivo, linha_busca)
                    trocou = True
                    break
            if not trocou:
                print("Não é possível resolver: zero na diagonal principal.")
                return None

        poe1numaLinhaDaRegiaoPreta(indice_pivo, matriz)

        for linha_atual in range(indice_pivo + 1, total_linhas):
            multiplicador = matriz[linha_atual][indice_pivo]
            for coluna in range(indice_pivo, total_linhas + 1):
                matriz[linha_atual][coluna] -= multiplicador * matriz[indice_pivo][coluna]

    solucao = [0] * total_linhas
    for linha in range(total_linhas - 1, -1, -1):
        soma = 0
        for coluna in range(linha + 1, total_linhas):
            soma += matriz[linha][coluna] * solucao[coluna]
        solucao[linha] = matriz[linha][total_linhas] - soma

    return solucao

def _gera_lentes_possiveis(valores_restantes, lente_atual, lentes_resultantes):
    if valores_restantes == []:
        lentes_resultantes.append(lente_atual)
    else:
        for indice_valor in range(len(valores_restantes)):
            _gera_lentes_possiveis(
                valores_restantes[0:indice_valor] + valores_restantes[indice_valor + 1:],
                lente_atual + [valores_restantes[indice_valor]],
                lentes_resultantes
            )

def gera_lentes_possiveis(valores):
    lentes = []
    _gera_lentes_possiveis(valores, [], lentes)
    return lentes

def gera_pares_de_lentes(lentes_possiveis):
    total_lentes = len(lentes_possiveis)
    pares = []
    for indice_linha in range(total_lentes):
        for indice_coluna in range(total_lentes):
            pares.append([lentes_possiveis[indice_linha], lentes_possiveis[indice_coluna]])
    return pares

def eh_bom(par_de_lentes, matriz):
    lente_linhas = par_de_lentes[0]
    lente_colunas = par_de_lentes[1]

    for indice in range(len(matriz)):
        if matriz[lente_linhas[indice]][lente_colunas[indice]] == 0:
            return False
    return True

def escolhe_a_melhor_lente(matriz):
    indices = list(range(len(matriz)))
    lentes_possiveis = gera_lentes_possiveis(indices)
    pares_de_lentes = gera_pares_de_lentes(lentes_possiveis)

    for indice_par in range(len(pares_de_lentes)):
        if eh_bom(pares_de_lentes[indice_par], matriz):
            return pares_de_lentes[indice_par]
    return []

def aplica_lente(matriz, lente_linha, lente_coluna):
    nova_matriz = []
    for indice_linha in lente_linha:
        nova_matriz.append([matriz[indice_linha][indice_coluna] for indice_coluna in lente_coluna] + [matriz[indice_linha][-1]])
    return nova_matriz

if __name__ == "__main__":
    caminho_arquivo = input("Digite o caminho completo do arquivo da matriz: ").strip()

    try:
        matriz_original = ler_matriz(caminho_arquivo)

        print("\nMatriz original lida:")
        mostrar_matriz(matriz_original)

        melhor_lente = escolhe_a_melhor_lente(matriz_original)

        if melhor_lente:
            lente_linhas, lente_colunas = melhor_lente
            matriz_com_lente = aplica_lente(matriz_original, lente_linhas, lente_colunas)

            print("\nMatriz com a melhor lente aplicada:")
            mostrar_matriz(matriz_com_lente)

            solucao = metodo_gauss(matriz_com_lente)

            if solucao:
                print("\nSolução do sistema:")
                nomes_variaveis = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q']
                for indice, valor in enumerate(solucao):
                    nome_variavel_original = nomes_variaveis[lente_colunas[indice]]
                    print(f"{nome_variavel_original} = {valor:.2f}")
        else:
            print("Nenhuma lente possível evita zeros na diagonal.")
    except FileNotFoundError:
        print("Erro: arquivo não encontrado. Verifique o caminho e tente novamente.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")
