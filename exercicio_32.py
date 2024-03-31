print("Desenvolva um programa que leia duas strings e verifique se elas são anagramas.\n")

def sao_anagramas(str1, str2):
    str1 = str1.replace('', '').lower()
    str2 = str2.replace('', '').lower()
    
    return sorted(str1) == sorted(str2)

str1 = 'cinema'
str2 = 'iceman'

if sao_anagramas(str1, str2):
    print(f" '{str1}' e '{str2}' são anagramas.")
else:
    print(f"'{str1}' e '{str2}'  não são anagramas.")