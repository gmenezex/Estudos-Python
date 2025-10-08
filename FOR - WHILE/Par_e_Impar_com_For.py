'''
Crie um programa que peça ao usuário um número inteiro positivo **N** e mostre a seguinte sequência:
- Todos os números de 1 até N
- Para cada número, indique se ele é **par** ou **ímpar**
'''

numero = int(input())

for n in range(1, numero+1):
  if n % 2 == 0:
    print(f'{n} - par')
  else:
    print(f'{n} - impar')
