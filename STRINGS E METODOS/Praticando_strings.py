'''
Crie um programa que:
1. Peça para o usuário digitar uma frase.
2. Mostre no console:
    - A frase toda em **maiúsculas**.
    - A frase toda em **minúsculas**.
    - A frase com a **primeira letra maiúscula**.
    - A quantidade de vezes que a letra **“a”** aparece.
    - A frase sem **espaços no início e no fim**.
    - A frase invertida.
'''

frase = input('Digite uma frase:')
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.count('a'))
print(frase.strip())
print(frase[::-1])