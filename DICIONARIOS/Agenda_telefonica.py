'''
Crie um programa que:
1. Permita cadastrar **vários contatos** de uma agenda.
    - Cada contato tem **nome** e **telefone**.
2. Armazene os contatos em um **dicionário**, onde a chave é o nome e o valor é o telefone.
3. Depois de cadastrar, permita ao usuário **consultar** o telefone de qualquer contato digitando o nome.
4. Se o contato não existir, mostre uma mensagem: `"Contato não encontrado"`.
'''

agenda = {}

while True:

  print('--MENU--\n')
  print('1 - Cadastrar contato\n')
  print('2 - Consultar contato\n')
  print('0 - Sair\n')

  opcao = int(input('Selecione: '))

  if opcao == 1:
    nome = input('Digite o nome: ')
    contato = int(input('Digite o número: '))
    agenda[nome] = contato
    print('Contato adicionado com sucesso!')

  elif opcao == 2:
    consulta = input('Digite o nome para consultar: ')

    if consulta in agenda.keys():
      print(f'Contato:{consulta} - {agenda.get(consulta)}')
    else:
      print('Contato não encontrado')

  elif opcao == 0:
    print('Saindo...')
    break
