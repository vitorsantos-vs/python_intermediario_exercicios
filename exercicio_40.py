print("Crie um programa que simule um sistema de votação eletrônico.\n")

class SistemaVotacao:
    def __init__(self):
        self.candidatos = {}
        self.total_votos = 0
        
    def adicionar_canditado(self, nome):
        self.candidatos[nome] = 0
        
    def votar(self, nome):
        if nome in self.candidatos:
            self.candidatos[nome] += 1
            self.total_votos += 1
            return True
        else:
            return False
        
    def resultado(self):
        for nome, votos in self.candidatos.items():
            porcentagem = (votos / self.total_votos) * 100
            print(f"{nome}: {votos} votos ({porcentagem:.2f}%)")
            
sistema = SistemaVotacao()
sistema.adicionar_canditado('Candidato 1')
sistema.adicionar_canditado('Candidato 2')

sistema.votar('Candidato 1')
sistema.votar('Candidato 1')
sistema.votar('Candidato 1')
sistema.votar('Candidato 1')
sistema.votar('Candidato 1')
sistema.votar('Candidato 2')
sistema.votar('Candidato 2')
sistema.votar('Candidato 2')

sistema.resultado()
