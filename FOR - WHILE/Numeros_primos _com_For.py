'''
Peça ao usuário um número inteiro positivo N e mostre todos os números primos entre 1 e N.
'''

numero = int(input('Digite um número inteiro para ver quantos primos ele tem:'))

for n in range(2,numero):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n, end=', ')

