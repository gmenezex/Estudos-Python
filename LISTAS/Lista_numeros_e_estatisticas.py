'''
Escreva um programa em Python que:

1. Peça ao usuário para digitar **10 números inteiros** e armazene-os em uma lista.
2. Mostre na tela:
    - A lista completa.
    - O maior e o menor número da lista.
    - A soma de todos os números.
    - A média dos números.
    - Apenas os números pares.
    - Apenas os números ímpares.
'''

numeros = []
maior = 0
menor = 0
soma = 0
pares = []
impares = []

for i in range(1, 11):
  numero = int(input(f'Digite o {i}° número: '))
  numeros.append(numero)

for n in numeros:
  if n % 2 ==0:
    pares.append(n)
  else:
    impares.append(n)
  soma += n

  if maior == 0 and menor == 0:
    maior = n
    menor = n
  
  if n > maior:
    maior = n
  elif n < menor:
    menor = n

print(f'Lista completa: {numeros}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Soma: {soma}')
print(f'Média: {soma / len(numeros)}')
print(f'Números pares: {pares} - qtd: {len(pares)}')
print(f'Números impares: {impares} - qtd: {len(impares)}')
