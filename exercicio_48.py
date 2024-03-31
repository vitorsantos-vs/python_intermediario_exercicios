print("Gerador de Planilhas: Desenvolva um programa que crie planilhas com dados fornecidos pelo usuário.\n")

import openpyxl
from openpyxl import Workbook

def criar_planilha(dados, nome_arquivo):
    wb = Workbook()
    ws = wb.active
    
    for linha in dados:
        ws.append(linha)
        
    wb.save(nome_arquivo)
    print(f"Planilha '{nome_arquivo} criada com sucesso.")
    
dados_usuario = [
    ["Nome", "Idade", "Profissão"],
    ["Vitor", 23, "Data Enginner"],
    ["Alice", 28, "Engenheira"],
    ["Bob", 34, "Designer"],
    ["Carol", 22, "Analista de Sistemas"]
]

nome_arquivo = "planilha_dados.xlsx"

criar_planilha(dados_usuario, nome_arquivo)
