import json
from fastapi import FastAPI
from Pessoa import Pessoa
from Produto import Produto
from pessoa_model import PessoaModelo
from produto_model import ProdutoModelo

p1 = Pessoa(
    '1',
    'JoãoPeba',
    '11/12/1998',
    'Proplayer de Valorant',
    'Gamer',
    'Solteiro',
    'Masculino',
    )

p2 = Pessoa(
    '2',
    'Laricela',
    '20/10/2006',
    'Cientista de Dados Sênior',
    'Superior',
    'Muito que bem',
    'Feminino'
    )

p3 = Pessoa(
    '3',
    'Matheus',
    '12/05/1999',
    'VideoMaker',
    'Superior',
    'Casado',
    'Masculino'
    )

p4 =  Pessoa(
    '4',
    'César',
    '31/12/2003',
    'Motorista de aplicativo',
    'Superior',
    'Casado',
    'Masculino'
    )


lista_pessoas = [
        p1,p2,p3,p4
    ]

pr1 = Produto(
    '1',
    'Teclado',
    'Periférico'
    )

pr2 = Produto(
    '2',
    'Mouse',
    'Periférico'
)

pr3 = Produto(
    '3',
    'Placa de Vídeo',
    'Componente'
)

pr4 = Produto(
    '4',
    'Cooler',
    'Componente'
)

pr5 = Produto(
    '5',
    'Pontos Riot',
    'GiftCard'
)

pr6 = Produto(
    '6',
    'Pontos Overwatch',
    'GiftCard'
)

lista_produtos = [
        pr1,pr2,pr3,pr4,pr5,pr6
]

app = FastAPI()#Variável classe FastAPI

#@ = Anotation, função que tem como parâmetro a função abaixo dela.
@app.get('/')
def minha_api():
    return 'Bem-vindo a minha API, para Usuários, acesse a rota /api/users'

@app.get('/api/users')
def users_api():
    return

@app.get('/api/v2/users')
def read_api(nome: str = ''):
    with open('user.json') as arquivos:
        users = json.loads(arquivos.read())
        
    if nome:
        filtered_users = []

        for user in users:
            if user['nome'].startswith(nome):
                filtered_users.append(user)
                
        return filtered_users
    
    return users
    
@app.get('/api/users/{id_pessoa}')
def get_pessoa(id_pessoa):
    for pessoa in lista_pessoas:
        if pessoa.id == id_pessoa:
            return pessoa
        
    return lista_pessoas[1]

@app.get('/api/v2/users/{id_pessoa}')
def get_pessoa(id_pessoa):
    with open('user.json') as arquivos:
        pessoas = json.loads(arquivos.read())
    
    for pessoa in pessoas:
        if pessoa.id == id_pessoa:
            return pessoa
        
    return "Pessoa não encontrada"

@app.get('/api/users/{nome_pessoa}')
def get_pessoa(nome_pessoa: str):
    for pessoa in lista_pessoas:
        if pessoa.nome == nome_pessoa:
            return pessoa
        
    return lista_pessoas[1]

@app.post('/api/v3/users/')
def post_pessoa(pessoa: PessoaModelo):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))
    
    pessoa.id = pessoas[-1]['id'] + 1
    pessoas.append(pessoa.model_dump())
    
    with open('user.json', 'w', encoding='utf-8') as arquivo:
        arquivo.write(json.dumps(pessoas, indent=4))

    return f'Pessoa com nome {pessoa.nome} criada com sucesso'

@app.delete('/api/v3/users/{id}')
def delete_pessoa(id: int):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))

    for posicao in range(len(pessoas)):
        print(posicao)
        if pessoas[posicao]['id'] == id:
            pessoas.pop(posicao)

            with open('user.json', 'w', encoding='utf-8') as arquivo:
                arquivo.write(json.dumps(pessoas, indent=4))

            return 'pessoa foi de vala'

    return 'pessoa nao existe'

@app.patch ('/api/v3/users/{id}')
def update_pesoas(id: int):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))

@app.get('/api/products')
def products_api():
    return

@app.get('/api/v2/products')
def read_api(nome_produto: str = ''):
    with open('product.json') as arquivos_produtos:
        products = json.loads(arquivos_produtos.read())
        
    if nome_produto:
        filtered_products = []

        for product in products:
            if product['nome_produto'].startswith(nome_produto):
                filtered_products.append(product)
                
        return filtered_products
    
    return products

@app.get('/api/v2/products/{id_produto}')
def get_produto(id_produto):
    with open('product.json') as arquivos_produto:
        produtos = json.loads(arquivos_produto.read())
    
    for produto in produtos:
        if produto['id'] == id_produto:
            return produto
        
    return "Produto não encontrado"

@app.get('/api/products/{nome_produto}')
def get_produto(nome_produto: str):
    for produto in lista_produtos:
        if produto["nome"] == nome_produto:
            return produto
        
    return lista_produtos[1]

@app.post('/api/v3/products/')
def post_product(produto: ProdutoModelo):
    with open('product.json', encoding='utf-8') as arquivo:
        produtos = list(json.loads(arquivo.read()))
    
    produto['id'] = produtos[-1]['id'] + 1
    produtos.append(produto.model_dump())
    
    with open('product.json', 'w', encoding='utf-8') as arquivo:
        arquivo.write(json.dumps(produtos, indent=4))

    return f'Pessoa com nome {produto['nome']} criada com sucesso'

@app.delete('/api/v3/products/{id_produto}')
def delete_produto(id_produto: int):
    with open('product.json', encoding='utf-8') as arquivo:
        produtos = list(json.loads(arquivo.read()))

    for posicao in range(len(produtos)):
        print(posicao)
        if int(produtos[posicao]['id']) == id_produto:#então, tive que pedir pro chatgpt me ajudar nessa parte, mas explicou bem bonitinho :)
            produtos.pop(posicao)

            with open('product.json', 'w', encoding='utf-8') as arquivo:
                arquivo.write(json.dumps(produtos, indent=4))

            return 'Produto deletado'

    return 'Produto não existe'

@app.patch ('/api/v3/users/{id_produto}')
def update_produtos(id_produto: int):
    with open('product.json', encoding='utf-8') as arquivo:
        produtos = list(json.loads(arquivo.read()))
