print("Escreva um programa que implemente o jogo da velha.\n")

def imprimir_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))
        print("-" * 10)

def verificar_vitoria(tab, jogador):
    for i in range(3):
        if all([tab[i][j] == jogador for j in range(3)]) or \
           all([tab[j][i] == jogador for j in range(3)]):
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] == jogador or \
       tab[0][2] == tab[1][1] == tab[2][0] == jogador:
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    turno = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        jogador_atual = jogadores[turno % 2]
        print(f"Vez do jogador {jogador_atual}")

        try:
            linha, coluna = map(int, input("Digite a linha e a coluna (0, 1 ou 2): ").split())
            if tabuleiro[linha][coluna] != " ":
                print("Posição já ocupada. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if all(all(celula != " " for celula in linha) for linha in tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        turno += 1

# Inicia o jogo
jogo_da_velha()
