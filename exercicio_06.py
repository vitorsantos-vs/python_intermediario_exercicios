print("Escreva um programa que implemente o algoritmo de busca em profundidade.\n")

def  busca_em_profundidade(grafo, no, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(no)
    print(no, end=' ')
    for vizinho in grafo[no]:
        if vizinho not in visitados:
            busca_em_profundidade(grafo, vizinho, visitados)
    return visitados

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visitados = busca_em_profundidade(grafo, 'A')
