print("Escreva um programa que implemente um conversor de moedas.\n")

def converter_moedas(taxa_cambio):
    valor = float(input("Digite o  valor a ser convertido: "))
    return valor * taxa_cambio

taxa_cambio =  float(input("Digite a taxa de câmbio atual: "))
print(f"O valor converter é {converter_moedas(taxa_cambio)}")
