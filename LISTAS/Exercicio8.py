'''
### Exercício Avançado

Dada a matriz (lista de listas):

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


Crie **em uma única list comprehension** uma lista contendo **apenas os números pares**, já elevados ao quadrado.
'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

lista = [n ** 2 for linha in matriz for n in linha if n % 2 == 0]
print(lista)