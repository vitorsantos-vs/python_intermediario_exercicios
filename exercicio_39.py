print("Crie um programa que simule um caixa eletrônico, com operações de saque, depósito e consulta de saldo.\n")

class CaixaEletronico:
    def __init__(self):
        self.saldo = 0
    
    def despositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False
        
    def sacar(self, valor):
        if self.saldo >= valor > 0:
            self.saldo -= valor
            return True
        return False
    
    def consultar_saldo(self):
        return self.saldo
    
def caixa_eletronico_interativo():
    caixa = CaixaEletronico()
    while True:
        print("\n1 - Depósito")
        print("2 - Saque")
        print("3 - Consultar saldo")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            if caixa.despositar(valor):
                print("Depósito realizado com sucesso.")
            else:
                print("Valor inválido.")
        elif opcao == 2:
            valor = float(input("Digite o valor do saque: "))
            if caixa.sacar(valor):
                print("Saque realizado com sucesso.")
            else:
                print("Saldo insuficiente ou valor  inválido.")
        elif opcao == 3:
            print("Seu saldo é R$", caixa.consultar_saldo())
        elif opcao == 4:
            break
        else:
            print("Opção inválida.")
            
caixa_eletronico_interativo()            
