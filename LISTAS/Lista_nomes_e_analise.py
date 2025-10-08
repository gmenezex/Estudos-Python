'''
Escreva um programa em Python que:
1. Peça ao usuário para digitar **5 nomes** e armazene-os em uma lista.
2. Mostre na tela:
    - A lista completa de nomes.
    - A lista em **ordem alfabética**.
    - A lista em **ordem inversa** (sem inverter a original).
    - Quantos nomes começam com a letra **"A"** (maiúscula ou minúscula).
    - O nome com **mais letras**.
    - O nome com **menos letras**.
'''

nomes = []
nomes_com_a = 0
nome_longo = None
nome_curto = None

for i in range(1, 6):
  nome = input(f'Digite o {i}º nome: ')
  nomes.append(nome)

nome_longo = nomes[0]
nome_curto = nomes[0]

for nome in nomes:
  if nome[0] == 'A' or nome[0] == 'a':
    nomes_com_a += 1

  if len(nome) > len(nome_longo):
    nome_longo = nome
  if len(nome) < len(nome_curto):
    nome_curto = nome

print(f'Lista completa: {nomes}')
print(f'Ordem alfabética: {sorted(nomes)}')
print(f'Ordem inversa: {list(reversed(nomes))}')
print(f'Nomes que começam com A: {nomes_com_a}')
print(f'Nome mais longo: {nome_longo}')
print(f'Nome mais curto: {nome_curto}')
