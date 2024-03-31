print("Escreva um programa que implemente o algoritmo de ordenação de inserção.\n")

def ordenacao_por_insercao(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
    
        while j >=0 and chave < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = chave

arr = [12, 11, 13, 5, 6, 7]
ordenacao_por_insercao(arr)

print("Array ordenado é:")
for i in range(len(arr)):
    print(f"{arr[i]}", end=' ')
    