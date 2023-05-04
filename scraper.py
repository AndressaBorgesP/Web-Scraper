import requests
from bs4 import BeautifulSoup

url = 'https://www.netshoes.com.br/tenis-adidas-breaknet-feminino-branco+preto-NQQ-4379-028'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.text, 'html.parser')


if site.status_code != 200:
    print(f'Erro ao fazer requisição: {site.status_code}')
    exit()


titulo = soup.select_one('.short-description h1').text.strip()
print('Título:', titulo)


preco = soup.select_one('.price').text.strip()
print('Preço:', preco)


descricao = soup.select_one('.feature-description-values').text.strip()
descricao = descricao.replace('Departamento BS:', '\nDepartamento BS:')
descricao = descricao.replace('Indicado para:', '\nIndicado para:')
descricao = descricao.replace('Estilo da Peça:', '\nEstilo da Peça:')
descricao = descricao.replace('Material:', '\nMaterial:')
descricao = descricao.replace('Material Interno:', '\nMaterial Interno:')
descricao = descricao.replace('Altura do Cano:', '\nAltura do Cano:')
print('Descrição:', descricao)


imagem = soup.select_one('.zoom')['src']
print('Imagem:', imagem)

with open('resultados.txt', 'w') as file:
    file.write(f'Título: {titulo}\n')
    file.write(f'Preço: {preco}\n')
    file.write(f'Descrição: {descricao}\n')
    file.write(f'Imagem: {imagem}\n')
