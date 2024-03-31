print("Escreva um programa que implemente o algoritmo de ordenação por contagem.\n")

def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m
    
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr

arr = [4, 2, 2, 8, 3, 3, 1, 5, 7, 6]
sorted_arr = counting_sort(arr)
print(f"Array ordenado: {sorted_arr}")
