print("Escreva um programa que implemente o algoritmo de ordenação por seleção.\n")

def ordenacao_por_selecao(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
arr = [64, 25, 12, 22, 11]
ordenacao_por_selecao(arr)

print("Array ordenado é:")
for i in range(len(arr)):
    print(f"{arr[i]}", end=" ")
    