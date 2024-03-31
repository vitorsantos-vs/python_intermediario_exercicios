print("Calculadora de Expressões Matemáticas: que possa avaliar expressões matemáticas simples fornecidas pelo usuário.\n")

import re

def calcular_expressao(expressao):
    expressao = expressao.replace(' ', '')

    if not re.match(r'^[\d\+\-\*\/\(\) ]+$', expressao):
        return "Expressão inválida. Por favor, insira uma expressão matemática correta."

    try:
        resultado = eval(expressao)
        return f"Resultado: {resultado}"
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    except Exception as e:
        return f"Erro: {str(e)}"

expressao_usuario = "(3 + 4) * 5 - 6 / (7 - 1)"
print(calcular_expressao(expressao_usuario))
