print("Validador de Expressão Regular: Desenvolva um programa que leia uma expressão regular e uma string e verifique se a expressão corresponde à string utilizando o módulo re.\n")

import re

def validar_regex(regex, string):
    padrao = re.compile(regex)
    if padrao.match(string):
        return "A string corresponde à expressão regular."
    else:
        return "A string não corresponde à expressão regular."
    
regex = input("Digite a expressão regular: ")
string = input("Digite a string: ")
print(validar_regex(regex, string))
