print("Escreva um programa que implemente o algoritmo de busca binária.\n")

def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            fim - meio + 1
        else:
            inicio = meio + 1
    return None

lista_ememplo = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
item_procurado = 9

indice_encontrado = busca_binaria(lista_ememplo, item_procurado)

if indice_encontrado is not None:
    print(f"Item encontrado no indice: {indice_encontrado}")
else:
    print(f"Item não encontrado na lsita.")
