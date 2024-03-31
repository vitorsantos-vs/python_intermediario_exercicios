print("Implemente um programa que crie um histograma a partir de uma lista de números.\n")

import matplotlib.pyplot as plt

def criar_histograma(numero):
    plt.hist(numero, bins=10, edgecolor='black')
    plt.title('Histograma dos Números')
    plt.xlabel('Número')
    plt.ylabel('Frequência')
    plt.show()
    
numeros = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
criar_histograma(numeros)
