def mostraJogo(jogadas):
    os.system('cls');
    print("\n**********  JOGO DA VELHA PAIR PROGRAMING  **********\n");

    for lin in range(3):
        for col in range(3):
            if (col == 2):
                print(f" {jogadas[lin][col]} ");
            else:
                print(f" {jogadas[lin][col]} ", end='|');
        if (lin != 2): print("---+---+---");

    print();


def ganhou(jogadas):
    for i in range(3):
        if jogadas[i][0] == jogadas[i][1] and jogadas[i][2] !=' ':
            return True
        else:
            for i in range(3):
                if jogadas[0][i]==jogadas[1][i] and jogadas[2][i] !=' ':
                    return True

                else:
                    return False
                    print("Deu velha!")

    # Coloque aqui a lógica para verificar se alguem ganhou


def deuVelha(jogadas):
    velha = False;
    # Coloque aqui a lógica para verificar se já deu velha

    return velha;


def trocaDeJogador(jog):
    if (jog == 'X'):
        return 'O';
    return 'X';


# ******** INICIO DO JOGO *************
import os

# Matrix de 3 linhas por 3 colunas
# para acessar uma posição de uma matriz, usamos 2 colchetes,
# um para a linha e outro para a coluna
jogadas = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]

vezDeQuem = 'X';
qtasJogadas = 9;

while (not ganhou(jogadas)
       and not deuVelha(jogadas)
       and qtasJogadas != 0):
    mostraJogo(jogadas);

    while True:
        try:
            linha  = int(input(f"Jogador {vezDeQuem}, deseja jogar em qual linha? "));
        except ValueError:
            print("\nUtilize apenas números!")
        else:
            if linha > 3 or linha==0:
                print("Utilize um valor entre 1 e 3!")
            else:
                break
    while True:
        try:
            coluna = int(input(f"Jogador {vezDeQuem}, deseja jogar em qual coluna? "));
        except ValueError:
            print("\nUtilize apenas números!")
        else:
            if coluna > 3 or linha == 0:
                print("Utilize um valor entre 1 e 3!")
            else:
                break
    if linha == 1:
        linha = 0
    elif linha == 2:
        linha = 1
    elif linha == 3:
        linha = 2

    if coluna == 1:
        coluna = 0
    elif coluna == 2:
        coluna = 1
    elif coluna == 3:
        coluna = 2

    del jogadas[linha][coluna]
    jogadas[linha].insert(coluna,vezDeQuem)
    qtasJogadas -= 1;
    vezDeQuem = trocaDeJogador(vezDeQuem);


# indique aqui qual jogador ganhou ou se deu velha