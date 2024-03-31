print("Escreva um programa que implemente um sistema de recomendação simples baseado em pontuações de usuários para filmes. O programa deve ser capaz de ler as pontuações de um arquivo, calcular a média de pontuação para cada filme e recomendar os filmes com as melhores médias.\n")

def ler_pontuacoes(arquivo):
    pontuacoes = {}
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            filme, usuario, pontuacao = linha.strip().split(',')
            if filme not in pontuacoes:
                pontuacoes[filme] = []
            pontuacoes[filme].append(int(pontuacao))
    return pontuacoes

def calcular_medias(pontuacoes):
    medias = {}
    for filme, pontos in pontuacoes.items():
        medias[filme] = sum(pontos) / len(pontos)
    return medias

def recomendar_filmes(medias):
    filmes_recomendados = sorted(medias.items(), key=lambda x: x[1], reverse=True)
    print("Filmes Recomendados:")
    for filme, media in filmes_recomendados:
        print(f"{filme}: {media:.2f}")

pontuacoes = ler_pontuacoes('pontuacoes.txt')
medias = calcular_medias(pontuacoes)
recomendar_filmes(medias)


