print("Conta Palavras em Arquivo: Desenvolva um programa que leia um arquivo de texto e retorne a quantidade de palavras no arquivo, ignorando pontuação.\n")

import string

def contar_palavras(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto.split()
    return len(palavras)

nome_arquivo = 'string.txt'
n_palavras = contar_palavras(nome_arquivo)
print(f"O arquivo contém {n_palavras} palavras.")
