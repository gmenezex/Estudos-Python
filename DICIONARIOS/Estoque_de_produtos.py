'''
Monte um programa que:

- Cadastre produtos e quantidades em um dicionário
- Permita atualizar quantidades (entrada/saída)
- Mostre o estoque atualizado
- Mostre o total de estoque
- Mostre o maior estoque
'''
estoque = {}

while True:
  nome_produto = input('Digite o nome do produto: ')
  quantidade = float(input('Digite a quantidade em estoque: '))

  if nome_produto not in estoque:
    estoque[nome_produto] = quantidade
  else:
    estoque[nome_produto] += quantidade
  
  novo_produto = input('Deseja cadastrar um novo produto (s) / (n): ')
  if novo_produto == 'n':
    break

total_estoque = sum(estoque.values())
maior_estoque = max(estoque, key=estoque.get)

print(estoque)
print(f'Total de estoque: {total_estoque}')
print(f'Produto com maior estoque: {maior_estoque} - {estoque.get(maior_estoque)}')