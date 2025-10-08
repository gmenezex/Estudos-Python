'''
Crie um programa que peça ao usuário **5 números inteiros** e no final mostre:
1. O maior número digitado
2. O menor número digitado
3. A média dos números
'''

maior_numero = 0
menor_numero = 0
soma = 0

for i in range(1,6):
    numero = int(input(f'Digite o {i}° número: '))
    if maior_numero == 0 and menor_numero == 0:
        maior_numero = numero
        menor_numero = numero

    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

    soma += numero


media = soma / 5
print(f'Maior número:{maior_numero}')
print(f'Menor número:{menor_numero}')
print(f'Média: {media}')
