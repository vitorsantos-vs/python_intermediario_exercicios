print("Cadastro de Funcionário: Crie um programa que leia os dados de um funcionário (nome, sobrenome, cargo, salário) e armazene essas informações em um dicionário.\n")

def cadastrar_funcionario():
    funcionario = {}
    funcionario['Nome'] = input("Digite o nome do funcionario: ")
    funcionario['sobrenome'] = input("Digite o sobrenome do funcionario: ")
    funcionario['cargo'] = input("Digite o cargo do funcionario: ")
    funcionario['salario'] = float(input("Digite o salário do funcionario: "))
    return funcionario

funcionario = cadastrar_funcionario()
print(funcionario)
