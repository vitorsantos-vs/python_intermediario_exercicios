print("Simulador de Máquina de Vendas Automáticas: Implemente um sistema que simule uma máquina de vendas, aceitando dinheiro e fornecendo produtos.\n")

class MaquinaVendas:
    def __init__(self, produtos, estoque, precos):
        self.produtos =  produtos
        self.estoque = estoque
        self.precos = precos
        self.dinheiro_inserido = 0
        
    def inserir_dinheiro(self, valor):
        self.dinheiro_inserido += valor
        return f"R${valor} inserido. Total inserido: R${self.dinheiro_inserido:.2f}"
    
    def selecionar_produto(self, produto):
        if produto not in self.produtos:
            return "Produto não disponivel."
        if self.estoque[produto] == 0:
            return "Produto esgotado."
        if self.dinheiro_inserido < self.precos[produto]:
            return "Dinheiro insuficiente."
        
        self.estoque[produto] -= 1
        self.dinheiro_inserido -= self.precos[produto]
        troco = self.dinheiro_inserido
        self.dinheiro_inserido = 0
        
        return f"Produto {produto} entregue. Troco: R${troco:.2f}"
    
    def reabastecer_produto(self, produto, quantidade):
        if produto not in self.produtos:
            return "Produto não disponivel."
        self.estoque[produto] += quantidade
        return f"Produto {produto} reabastercido. Quantidade atual: {self.estoque[produto]}"
    
produto = ["Refrigerante", "Chocolate", "Chips"]
estoque = {"Refrigerante" : 10, "Chocolate" : 5, "Chips" : 8}
precos = {"Refrigerante" : 3.00, "Chocolate" : 2.50, "Chips" : 2.00}

maquina = MaquinaVendas(produto, estoque, precos)

print(maquina.inserir_dinheiro(5.00))
print(maquina.selecionar_produto("Chocolate"))

print(maquina.reabastecer_produto("Chocolate", 10))            
