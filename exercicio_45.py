print("Sistema de Análise de Texto: Escreva um programa que analise textos fornecidos pelo usuário, fornecendo estatísticas como contagem de palavras e frequência de palavras-chave.\n")

def analisar_texto(texto):
    texto = ''.join([caractere.lower() for caractere in texto if caractere.isalpha() or caractere.isspace()])

    palavras = texto.split()
    
    contagem_palavras = {}
    for palavra in  palavras:
        if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
        else:
            contagem_palavras[palavra] = 1
            
    palavra_ordenada = sorted(contagem_palavras.items(), key=lambda item: item[1], reverse=True)

    total_palavras = len(palavras)
    
    return total_palavras, palavra_ordenada

texto_exemplo = "Como usuário, quero poder inserir um texto e obter estatísticas sobre o texto, como o número total de palavras e a frequência de cada palavra."
total_palavras, frequencia_palavras = analisar_texto(texto_exemplo)

print(f"Número total de palavras: {total_palavras}")
print("Frequência das palavras:")
for palavras, frequencia in frequencia_palavras:
    print(f"{palavras}: {frequencia}")
    