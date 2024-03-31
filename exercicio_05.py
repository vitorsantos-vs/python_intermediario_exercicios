print("Escreva um programa que implemente o algoritmo de ordenação mergesort.\n")

def marge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        
        marge_sort(esquerda)
        marge_sort(direita)
        
        i = j = k = 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1
        
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
            
    return lista

lista_exemplo = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = marge_sort(lista_exemplo)

print(f"Lista ordenda: {lista_ordenada}")
