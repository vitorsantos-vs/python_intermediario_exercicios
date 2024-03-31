print("Escreva um programa que implemente o algoritmo de busca em largura.\n")

from collections import deque

def busca_em_largura(grafo, no_inicial):
    visitados = set()
    fila = deque([no_inicial])

    while fila:
        no = fila.popleft()
        if no not in visitados:
            print(no)
            visitados.add(no)
            
            vizinhos = grafo.get(no, [])
            for vizinho in vizinhos:
                if vizinho not in visitados:
                    fila.append(vizinho)
    return visitados

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': []
}

visitados = busca_em_largura(grafo, 'A')
print("Nós visitados:", visitados)
