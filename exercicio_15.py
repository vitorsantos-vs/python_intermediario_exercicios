print("Escreva um programa que implemente o algoritmo de criptografia Caesar Cipher.\n")

def cifra_cesar(texto, deslocamento, direcao):
    resultado = ""
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letra in texto.upper():
        if letra in alfabeto:
            posicao_atual = alfabeto.find(letra)
            if direcao == "criptografar":
                nova_posicao = (posicao_atual + deslocamento) % 26
            elif direcao == "descriptografar":
                nova_posicao = (posicao_atual - deslocamento) % 26
            resultado += alfabeto[nova_posicao]
        else:
            resultado += letra

    return resultado

# Exemplo de uso:
texto_original =  input("Digite uma frase: ")
deslocamento = int(input("Digite o deslocamento: "))

texto_criptografado = cifra_cesar(texto_original, deslocamento, "criptografar")
print("Texto Criptografado:", texto_criptografado)

texto_descriptografado = cifra_cesar(texto_criptografado, deslocamento, "descriptografar")
print("Texto Descriptografado:", texto_descriptografado)

