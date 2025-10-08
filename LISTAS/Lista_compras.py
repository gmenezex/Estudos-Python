'''
Escreva um programa em Python que:

1. Crie uma lista inicial com **5 itens de supermercado** (ex: arroz, feijão, leite, pão, café).
2. Mostre a lista completa.
3. Peça ao usuário:
    - Um **novo item** para **adicionar ao final da lista**.
    - Um **item existente** para **remover da lista**.
    - Um **item existente** e um **novo item** para **substituir**.
4. Mostre a lista final após as alterações.
'''

carrinho = ['arroz', 'feijão', 'leite', 'pão', 'café']
print(f'Lista inicial: {carrinho}')

novo_item = input('Digite um item para adicionar: ')
carrinho.append(novo_item)

remove_item = input('Digite um item para remover: ')
carrinho.remove(remove_item)

subs_item = input('Digite o item a ser substituido: ')
novo_item = input('Digite o novo item: ')

indice = carrinho.index(subs_item)
carrinho[indice] = novo_item

print(f'Lista final: {carrinho}')
