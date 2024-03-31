print("Conversor de Bases Numéricas: Implemente um programa que leia um número inteiro e permita a conversão desse número entre as bases binária, octal, decimal e hexadecimal.\n")

def conveter_base(numero, base):
    if base == 'bin':
        return bin(numero)[2:]
    elif base == 'oct':
        return oct(numero)[2:]
    elif base == 'dec':
        return str(numero)
    elif base == 'hex':
        return hex(numero)[2:]
    else:
        raise ValueError("Base não reconhecida.")
    
numero = int(input("Digite um númeor inteiro: "))
base = input("Digite a base para conversão (bin, oct, dec, hex): ").lower()

try:
    numero_convertido = conveter_base(numero, base)
    print(f"O número {numero} na base {base} é: {numero_convertido}")
except ValueError as e:
    print(e)
    