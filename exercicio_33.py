print("Implemente um programa que leia uma lista de produtos e calcule o valor total da compra.\n")

def calcular_total_compra(lista_produtos):
    total = 0
    for produto in lista_produtos:
        total += produto['quantidade'] * produto['preco']
    return total

lista_produtos = [
    {'nome': 'Produto 1', 'quantidade': 2, 'preco': 10.0},
    {'nome': 'Produto 2', 'quantidade': 1, 'preco': 20.0},
    {'nome': 'Produto 3', 'quantidade': 3, 'preco': 15.0},
]

total = calcular_total_compra(lista_produtos)
print(f"Valor Total da Compra é: R${total:.2f}") 
