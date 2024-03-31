print("Implementa um simples raspador de web usando BeautifulSoup e requests. Este código tenta raspar URLs de uma página web\n")

from bs4 import BeautifulSoup
import requests

def scrape_website(url):
    # Envia um pedido GET para a URL
    response = requests.get(url)
    
    # Verifica se o pedido foi bem-sucedido
    if response.status_code == 200:
        # Analisa o conteúdo HTML da página usando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontra todas as tags 'a' (que definem hiperligações)
        links = soup.find_all('a')
        
        # Extrai o atributo href (URL) de cada tag 'a'
        urls = [link.get('href') for link in links if link.get('href') is not None]
        
        # Retorna a lista de URLs
        return urls
    else:
        # Se o pedido não foi bem-sucedido, retorna uma mensagem de erro
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"

# Exemplo de uso: Raspar a lista de URLs da homepage do Python.org
scraped_urls = scrape_website('https://www.python.org')

# Imprime a lista de URLs
print("Lista de URLs encontradas na homepage do Python.org:")
for url in scraped_urls:
    print(url)

