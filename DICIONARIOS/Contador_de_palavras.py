'''
Crie um programa que:

1. Peça ao usuário para digitar uma frase.
2. Conte quantas vezes cada palavra aparece na frase.
3. Guarde essas informações em um **dicionário**, onde:
    - a **chave** é a palavra
    - o **valor** é a quantidade de vezes que ela aparece
4. Mostre o dicionário no final.
'''

frase = input('Digite uma frase: ').lower().split()

palavras = {}

for palavra in frase:
  if palavra not in palavras:
    palavras[palavra] = 1
  else:
    palavras[palavra] += 1

print(palavras.items())