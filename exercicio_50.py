print("Crie um programa que leia dados de vendas de um arquivo CSV e gere um relatório com o total de vendas por produto e por vendedor. O arquivo CSV terá colunas para o nome do vendedor, o produto vendido e o valor da venda de forma visual.\n")

import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def gerar_relatorio(nome_arquivo_csv):
    vendas_por_produto = defaultdict(float)
    vendas_por_vendedor = defaultdict(float)

    with open(nome_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            vendedor = linha['nome do vendedor']
            produto = linha['produto vendido']
            valor = float(linha['valor da venda'])

            vendas_por_produto[produto] += valor
            vendas_por_vendedor[vendedor] += valor

    produtos = list(vendas_por_produto.keys())
    vendas_produtos = list(vendas_por_produto.values())
    plt.figure(figsize=(10, 8))
    plt.bar(produtos, vendas_produtos, color='blue')
    plt.title('Total de Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Valor de Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    vendedores = list(vendas_por_vendedor.keys())
    vendas_vendedores = list(vendas_por_vendedor.values())
    plt.figure(figsize=(10, 8))
    plt.bar(vendedores, vendas_vendedores, color='green')
    plt.title('Total de Vendas por Vendedor')
    plt.xlabel('Vendedor')
    plt.ylabel('Valor de Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

gerar_relatorio('dados_vendas.csv')
