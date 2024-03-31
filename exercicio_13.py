print("Manipulação de Strings: Escreva um programa que inverta a ordem das palavras em uma string fornecida pelo usuário.\n")

string_usuario = input("Digite uma frase: ")

string_ivertida = ' '.join(string_usuario.split()[::-1])

print("A frase com a ordem das palavras invertida é:")
print(string_ivertida)
