'''
Crie um programa que peça um número inteiro e mostre o fatorial dele.
'''

numero = int(input('Digite um número: '))
fator = 1

for i in range(1, numero + 1):
    fator *= i

print(fator)
