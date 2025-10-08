'''
1. Peça ao usuário para digitar **vários nomes** separados por vírgula.
2. Use `split()` para transformar esses nomes em uma lista.
3. Mostre os nomes de duas formas diferentes:
    - Um por linha.
    - Todos juntos, mas separados por  (hífen).
'''

nome = input('Digite alguns nomes, separando eles por vírgula: ')
lista_nomes = nome.split(',')

print(lista_nomes)

for n in lista_nomes:
  print(n.strip())

print('Nomes separados por hífen')
print(f'{'-'.join(lista_nomes).strip()}')
