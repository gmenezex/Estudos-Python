'''
Escreva um programa em Python que:

1. Crie uma lista inicial com **5 preços de produtos** (ex: 10.50, 25.00, 7.30, 15.90, 5.00).
2. Mostre a lista completa.
3. Peça ao usuário:
    - Um **novo preço** para **adicionar ao final da lista**.
    - Um **preço existente** para **remover da lista**.
    - Um **preço existente** e um **novo preço** para **substituir**.
4. Ao final, mostre:
    - A lista final de preços.
    - O **total da compra** (soma dos preços).
    - O **preço médio**.
    - O **maior** e o **menor preço** da lista
'''

precos = [10.50, 25.00, 7.30, 15.90, 5.00]

print(f'Lista de preços: {precos}')

novo_preco = float(input('Digite um preço para adicionar: '))
precos.append(novo_preco)

remove_preco = float(input('Digite um preço para remover: '))
if remove_preco in precos:
  precos.remove(remove_preco)
else:
  print(f'O preço {remove_preco:.2f} não está na lista')

subs_preco = float(input('Digite um preço para substituir: '))
if subs_preco in precos:
  novo_preco = float(input('Digite o novo preço: '))
  indice = precos.index(subs_preco)
  precos[indice] = novo_preco
else:
  print(f'O preço {subs_preco:.2f} não está na lista')

total = sum(precos)
maior_preco = max(precos)
menor_preco = min(precos)
preco_medio = total / len(precos)

print(f'\nLista de preços final: {precos}')
print(f'Total da compra: R$ {total:.2f}')
print(f'Média de preços: R$ {preco_medio:.2f}')
print(f'Maior preço da lista: R$ {maior_preco:.2f}')
print(f'Menor preço da lista: R$ {menor_preco:.2f}')
