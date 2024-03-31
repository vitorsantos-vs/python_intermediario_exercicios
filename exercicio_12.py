print("Escreva um programa que implemente o algoritmo de busca sequencial.\n")

def busca_sequencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1

lista_numeros = [5, 3, 7, 1, 4, 9,]
item_procurado = 9

resultado = busca_sequencial(lista_numeros, item_procurado)

if resultado != -1:
    print(f"Item encontrado índice {resultado}")
else:
    print("Item não encontrado na lista.")
    