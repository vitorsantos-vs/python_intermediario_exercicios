print("Escreva um programa que encontre o caminho mais curto em um gráfico usando o algoritmo de Dijkstra.\n")

import heapq

def dijkstra(grafo, inicio):
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue
        
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                
        heapq.heappush(fila_prioridade, (distancia, vizinho))
    return distancias

grafo_exemplo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

inicio = 'A'
caminho = dijkstra(grafo_exemplo, inicio)

print(f"Distancia do ponto de início '{inicio}': {caminho}")
