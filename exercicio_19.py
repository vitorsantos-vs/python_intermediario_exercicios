def flip(arr, i):
    """Função auxiliar para 'virar' o array até o índice i."""
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max(arr, n):
    """Encontra o índice do maior elemento no array até o índice n."""
    max_index = 0
    for i in range(1, n + 1):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    """Ordena o array usando o algoritmo de ordenação por pancake."""
    n = len(arr)
    while n > 1:
        # Encontra o maior elemento no array não ordenado
        max_index = find_max(arr, n - 1)

        # Se o maior elemento não estiver na posição correta, mova-o para lá
        if max_index != n - 1:
            # Vira o array do início até o maior elemento
            flip(arr, max_index)
            # Vira o array inteiro, movendo o maior elemento para a posição correta
            flip(arr, n - 1)
        
        # Reduz o tamanho do array não ordenado
        n -= 1
    return arr

# Exemplo de uso
arr = [3, 6, 2, 7, 5, 8, 4, 1]
sorted_arr = pancake_sort(arr)
print('Array ordenado:', sorted_arr)
