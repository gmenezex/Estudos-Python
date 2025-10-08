'''
Faça um programa que:
1. Peça ao usuário para digitar uma frase.
2. Mostre no console:
    - Quantas **palavras** existem na frase.
    - A **primeira palavra** e a **última palavra**.
    - A frase toda com as palavras **em ordem inversa**.
    - A frase com todas as palavras unidas por **hífens (-)** em vez de espaços.
'''

frase = input('Digite uma frase: ')
palavras = frase.split()
print(f'FRASE ORIGINAL: {frase}')
print(f'Quantidade de palavras: {len(palavras)}')
print(f'Primeira palavra: {palavras[0]}')
print(f'Ultima palavra: {palavras[-1]}')
print(f'Palavras invertidas: {' '.join(palavras[::-1])}')
print(f'Frase com hífens: {'-'.join(palavras)}')