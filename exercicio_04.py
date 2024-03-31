print("Escreva um programa que implemente o algoritmo de ordenação quicksort.\n")

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x < pivo]
        maiores = [x for x in lista[1:] if x >= pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

lista_exemplo = [33, 2, 73, 25, 14, 56, 15, 47, 82, 22]
lista_ordenada = quicksort(lista_exemplo)

print(f"Lista ordenada: {lista_ordenada}")
