'''
### Filtrar estoque por inicial

Dado o dicionário:

estoque = {
    "Arroz": 20,
    "Feijao": 8,
    "Macarrao": 5,
    "Leite": 4.5,
    "Azeite": 15
}

Crie uma lista apenas com os produtos que **começam com a letra "A"**.
'''
estoque = {
    "Arroz": 20,
    "Feijao": 8,
    "Macarrao": 5,
    "Leite": 4.5,
    "Azeite": 15
}

novo_estoque = [(produto, preco) for produto, preco in estoque.items() if produto[0] == 'A']

print(novo_estoque)