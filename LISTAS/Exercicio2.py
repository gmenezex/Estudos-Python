'''
Quadrados dos números

Dada uma lista de números `[1, 2, 3, 4, 5]`, gere outra lista contendo o quadrado de cada número.
'''
numeros = [1, 2, 3, 4, 5]

quadrados = [n ** 2 for n in numeros]
print(quadrados)