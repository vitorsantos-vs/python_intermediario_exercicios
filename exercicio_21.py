print("Desenvolva um programa que leia uma lista de nomes e retorne o nome mais curto.\n")

def nome_mais_curto(lista_de_nomes):
    mais_curto = lista_de_nomes[0]
    
    for nome in lista_de_nomes:
        if len(nome) < len(mais_curto):
            mais_curto = nome
    return mais_curto

nomes = ["Ana", "Arthur", "Vitor", "Stephanie", "Pedro", "Mariana", "Lu"]

print(f"O nome mais curto é: {nome_mais_curto(nomes)}")
