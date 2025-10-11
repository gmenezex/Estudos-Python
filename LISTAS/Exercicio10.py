'''
**Cadastro de nomes**

Crie um programa que:

1. Peça ao usuário para digitar 5 nomes.
2. Guarde esses nomes em uma **lista**.
3. Crie uma função que receba essa lista e mostre todos os nomes em letras maiúsculas.
'''

nomes = []

for i in range(1, 6):
  nome = input(f'Digite o {i}º nome: ')
  nomes.append(nome)

def maisculo(nomes):
  nomes_maisculo = [nome.upper() for nome in nomes]
  print(f'Nomes em maiúsculo: {nomes_maisculo}')

maisculo(nomes)