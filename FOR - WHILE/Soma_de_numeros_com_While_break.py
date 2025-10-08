'''
Faça um programa que peça ao usuário vários números inteiros.
O programa deve parar **quando o usuário digitar 0** e ao final mostrar 
a soma de todos os números digitados (sem contar o 0).
'''

total = 0

while True:
    numero = int(input('Digite um número (0 para parar): '))
    if numero == 0:
        break
    else:
        total += numero

print(f'A soma dos números é: {total}')
