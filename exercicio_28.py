print("Crie um programa que simule o lançamento de um dado e conte a frequência de cada face.\n")

import random
from collections import Counter

def lancar_dados(n_vezes):
    resultado = []
    for _ in range(n_vezes):
        resultado.append(random.randint(1, 6))
    return resultado

def contar_frequencia(resultado):
    return Counter(resultado)

n_vezes = 1000
resultado = lancar_dados(n_vezes)
frequencia = contar_frequencia(resultado)

for face, frequencia in frequencia.items():
    print(f"Face {face}: {frequencia} vezes")
