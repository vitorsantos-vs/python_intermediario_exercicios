print("Escreva um programa que implemente o algoritmo de ordenação bubble sort.\n")

def buuble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocado = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocado = True
        if not trocado:
            break
    return lista

lista_exemplo = [64, 34, 25, 12, 22, 11, 90, 5, 56, 48]
lista_ordenada = buuble_sort(lista_exemplo)

print(f"Lista ordenada: {lista_ordenada}")
