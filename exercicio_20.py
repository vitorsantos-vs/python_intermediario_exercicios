print("Crie um programa que leia uma string e conte o número de vogais e consoantes.\n")

def contar_vogais_consoantes(texto):
    vogais = 'aeiouAEIOU'
    
    contagem_vogais = 0
    contagem_consoantes = 0
    
    for  letra in texto:
        if letra.isalpha():
            if  letra in vogais:
                contagem_vogais += 1
            else:
                contagem_consoantes += 1
                
    return contagem_vogais, contagem_consoantes

texto_usuario = input("Digite uma string: ")
vogais, consoantes = contar_vogais_consoantes(texto_usuario)
print(f"Vogais: {vogais}, Consoantes: {consoantes}")
