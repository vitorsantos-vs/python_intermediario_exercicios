print("Implemente um programa que simule um jogo de bingo.\n")

import random

def gerar_cartela():
    cartela = [random.sample(range(i, i+10), 5) for i in range(1, 51, 10)]
    return cartela

def sortear_numero():
    return random.randint(1, 60)

def marcar_numero(cartela, numero):
    for linha in cartela:
        if numero in linha:
            linha[linha.index(numero)] = 'X'
            return True
    return False

def verificar_bingo(cartela):
    for linha in cartela:
        if all(el == 'X' for el in linha):
            return True
    return False

cartela = gerar_cartela()
print('Cartela inicial', cartela)

for _ in range(60):
    numero_sorteado = sortear_numero()
    marcar_numero(cartela, numero_sorteado)
    if verificar_bingo(cartela):
        print("BINGO")
        break

print("Cartela final: ", cartela)
