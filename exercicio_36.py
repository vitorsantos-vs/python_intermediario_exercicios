print("Desenvolva um programa que leia uma data (dia, mês e ano) e calcule a diferença de dias entre essa data e a data atual.\n")

from datetime import datetime

def calcular_diferenca_dias(data):
    data_atual = datetime.now()
    data = datetime.strptime(data, '%d/%m/%Y')
    diferenca = data_atual - data
    return diferenca.days

data = '23/01/2001'
dias = calcular_diferenca_dias(data)

print(f'A diferença entre a data atual e {data} é de {dias} dias.')
