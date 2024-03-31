print("Crie um programa que simule um sistema de reservas de hotel.\n")

import datetime

class SistemaReservaHotel:
    def __init__(self):
        self.reserva = {}
        
    def reservar_quarto(self, nome_hospede, numero_quarto, data_entrada, data_saida):
        if numero_quarto in self.reserva:
            for datas in self.reserva[numero_quarto]:
                if data_entrada <= datas[1] and data_saida >= datas[0]:
                    return f"Quarto {numero_quarto} já está reservado para data informadas."
        else:
            self.reserva[numero_quarto] = []
            
        self.reserva[numero_quarto].append((data_entrada, data_saida))
        return f"Quarto {numero_quarto} reservado com sucesso para {nome_hospede} de {data_entrada} até {data_saida}."
    
    def verificar_disponibilidade(self, numero_quarto, data):
        if numero_quarto in self.reserva:
            for datas in self.reserva[numero_quarto]:
                if datas[0] <= data <= datas[1]:
                    return f"Quarto {numero_quarto} não está disponivel em {data}."
        return f"Quarto {numero_quarto} está disponivel em {data}."
    
hotel = SistemaReservaHotel()

print(hotel.reservar_quarto("Vitor Santos", 101, datetime.date(2024, 12, 20), datetime.date(2024, 12, 31)))

print(hotel.verificar_disponibilidade(101, datetime.date(2024, 12, 21)))
