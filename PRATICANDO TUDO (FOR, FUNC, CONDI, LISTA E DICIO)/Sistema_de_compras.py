'''
Crie um programa que simule o carrinho de compras de um mercado.

Regras:
1. O programa deve ter um **dicionário** chamado `estoque`, onde as **chaves** são os nomes dos produtos e os **valores** são os preços.
    estoque = {
        "Arroz": 20.0,
        "Feijão": 8.5,
        "Macarrão": 5.0,
        "Leite": 4.5
    }
2. O usuário terá um **carrinho (lista)** para adicionar os produtos escolhidos.
3. O programa deve ter um **menu (while)** com as opções:
    - `1 - Listar produtos disponíveis`
    - `2 - Adicionar produto ao carrinho`
    - `3 - Mostrar carrinho e valor total`
    - `4 - Finalizar compra e sair`
4. Deve usar pelo menos **uma função** para calcular o valor total da compra.
5. Deve usar **for** para percorrer o carrinho e/ou o estoque.
6. Deve usar **if/else** para validar se o produto existe antes de adicionar ao carrinho.
'''
estoque = {
  "Arroz": 20.0,
  "Feijão": 8.5,
  "Macarrão": 5.0,
  "Leite": 4.5
}

menus = [
  '1 - Listar produtos disponíveis', 
  '2 - Adicionar produto ao carrinho', 
  '3 - Mostrar carrinho e valor total',
  '4 - Finalizar compra e sair'
]

carrinho = []

def listar_produtos():
  print('\n*PRODUTOS DISPONIVEIS*')
  for produto, preco in estoque.items():
    print(f'{produto} - R$ {preco:.2f}')

def adicionar_produto(produto):
  carrinho.append((produto,estoque.get(produto)))
  print(f'{produto} adicionado ao carrinho !')

def total_carrinho():
  valor_no_carrinho = 0
  if not carrinho:
    print('Carrinho está vazio.')
    return
  else:
    for produto, preco in carrinho:
      print(f'{produto} -> R$ {preco:.2f}')
      valor_no_carrinho += preco
  print(f'TOTAL: R$ {valor_no_carrinho:.2f}')

def sub_total():
  if not carrinho:
    print('Carrinho está vazio.')
    return
  total = sum(preco for _, preco in carrinho)
  print(f'Compra finalizada! Total a pagar: R$ {total:.2f}')

while True:
  print('\n----- MENU -----')
  for menu in menus:
    print(menu)

  try:
    opcao = int(input('Selecione: '))

    if opcao == 1:
      listar_produtos()

    elif opcao == 2:
      produto = input('Digite o produto para adicionar ao carrinho: ').capitalize()

      if produto in estoque:
        adicionar_produto(produto)
      else:
        print('Produto não está disponível')

    elif opcao == 3:
      total_carrinho()

    elif opcao == 4:
      sub_total()
      break
  
    else:
      print('Digite uma opção valida.')

  except ValueError:
    print('Digite somente números.')