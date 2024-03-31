print("Escreva um programa que implemente um sistema de reserva de bilhetes.\n")

class SistemaReservaBilhetes:
    def __init__(self):
        self.bilhetes_reservado = []
        
    def reservar_bilhete(self, nome_cliente):
        if nome_cliente not in self.bilhetes_reservado:
            self.bilhetes_reservado.append(nome_cliente)
            return f"Bilhete reservado com sucesso para {nome_cliente}."
        else:
            return f"Erro: Já existe uma reserva no nome de {nome_cliente}."
        
    def verificar_disponibilidade(self, nome_cliente):
        return nome_cliente not in self.bilhetes_reservado
    
    def cancelar_reserva(self, nome_cliente):
        if nome_cliente in self.bilhetes_reservado:
            self.bilhetes_reservado.remove(nome_cliente)
            return f"Reserva cancelada com sucesso para {nome_cliente}."
        else:
            return f"Erro: Não há reserva no nome de {nome_cliente}."
        
sistema = SistemaReservaBilhetes()

print(sistema.reservar_bilhete("Alice"))
print(sistema.reservar_bilhete("Bob"))

print(sistema.verificar_disponibilidade("Alice"))  
print(sistema.verificar_disponibilidade("Carlos"))

print(sistema.cancelar_reserva("Alice"))
print(sistema.cancelar_reserva("Carlos"))     
