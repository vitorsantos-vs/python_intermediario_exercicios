print("Simulador de Pedágio: Desenvolva um programa que leia o tipo de veículo (carro, moto, caminhão) e a quantidade de eixos, e calcule o valor do pedágio de acordo com a tabela de preços.\n")

# Simulador de Pedágio

def calcular_pedagio(tipo_veiculo, qtd_eixos):
    # Tabela de preços fictícia
    precos = {
        'carro': 5.00,
        'moto': 2.50,
        'caminhao': 10.00, # Preço base para caminhão com dois eixos
    }
    
    # Calcula o preço do pedágio
    if tipo_veiculo in precos:
        if tipo_veiculo == 'caminhao':
            # Adiciona o custo adicional por eixo extra
            preco_final = precos[tipo_veiculo] + (qtd_eixos - 2) * 5.00
        else:
            preco_final = precos[tipo_veiculo]
    else:
        raise ValueError("Tipo de veículo não reconhecido.")
    
    return preco_final

# Exemplo de uso
tipo_veiculo = input("Digite o tipo de veículo (carro, moto, caminhão): ").lower()
qtd_eixos = int(input("Digite a quantidade de eixos (se aplicável): "))

try:
    valor_pedagio = calcular_pedagio(tipo_veiculo, qtd_eixos)
    print(f"O valor do pedágio para um {tipo_veiculo} com {qtd_eixos} eixos é: R$ {valor_pedagio:.2f}")
except ValueError as e:
    print(e)
