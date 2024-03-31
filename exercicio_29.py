print("Desenvolva um programa que leia um arquivo CSV e imprima seu conteúdo na tela.\n")

import csv

def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)
            
nome_arquivo = 'teste.csv'
ler_csv(nome_arquivo)
