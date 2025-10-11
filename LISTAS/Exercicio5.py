'''
### Filtrar dicionário

Dado o dicionário:

precos = {"arroz": 20, "feijao": 8, "macarrao": 5, "leite": 4.5}

Use compreensão de listas para gerar uma lista apenas com os produtos cujo preço seja maior que 5.
'''
precos = {"arroz": 20, "feijao": 8, "macarrao": 5, "leite": 4.5}

maior_cinco = [(produto, preco) for produto, preco in precos.items() if preco > 5]
print(maior_cinco)