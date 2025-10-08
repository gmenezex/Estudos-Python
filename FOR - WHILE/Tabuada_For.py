'''
Crie um programa que peça um número inteiro positivo e mostre a tabuada dele de 1 a 10.
Esse sistema contem uma variável do tipo int, na qual o usuário digita o seu valor.
Sistema vai fazer um for, utilizando o range com dois parâmetros. 
Primeiro parâmetro o valor que a iteração (i) vai começar e o segundo até qual número ele deve percorrer.
'''

numero = int(input('Digite um número para ver sua tabuada de 1 a 10: '))

for i in range(1, 11):
    print(f'{numero} X {i} = {numero * i}')
