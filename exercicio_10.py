print("Implemente um programa que leia uma lista de números e a ordene de forma decrescente.\n")

entrada_usuario = input("Digite uma lista de número sepado por espaço: ")

lista_numero = [int(num) for num in  entrada_usuario.split()]

lista_numero.sort(reverse=True)

print("Lista ordenada de forma decresente:")
print(lista_numero)
