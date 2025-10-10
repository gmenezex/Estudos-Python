'''
Crie um dicionário de 3 filmes e seus anos de lançamento. Depois:

- adicione 1 filme,
- altere o ano de 1 filme,
- remova outro,
- percorra o dicionário imprimindo tudo.
'''

filmes = {
  'Os Vingadores': 2012,
  'Vingadores: Era de Ultron': 2015,
  'Vingadores: Guerra Infinita': 2018,
}

novo_filme = input('Digite o nome do filme para adicionar: ')
ano_filme = int(input('Digite o ano de lançamento do filme: '))

filmes[novo_filme] = ano_filme

editar_filme = input('Digite o nome do filme que quer alterar o ano: ')
if editar_filme in filmes:
  editar_ano = int(input(f'Informe o ano do {editar_filme}: '))
  filmes[editar_filme] = editar_ano
else:
  print(f'{editar_filme} não encontrado no catalogo')

remover_filme = input('Digite o nome do filme que deseja remover: ')
if remover_filme in filmes:
  del filmes[remover_filme]
  print(f'Filme: {remover_filme} removido!')
else:
  print(f'{editar_filme} não encontrado no catalogo')


for filme, ano in filmes.items():
  print(f'{filme} - Ano: {ano}')