'''
Regras:

1. O programa deve armazenar os alunos em um **dicionário**, onde:
    - a **chave** é o nome do aluno
    - o **valor** é uma **lista de notas**.
2. O programa deve ter um **menu** (usando `while`) com as opções:
    - `1 - Adicionar aluno e suas notas`
    - `2 - Listar todos os alunos e suas notas`
    - `3 - Mostrar a média de um aluno específico`
    - `4 - Sair`
3. Você deve usar pelo menos **uma função** (ex: para calcular média, para exibir dados, etc.).
4. O programa deve usar **for** para percorrer as listas de notas e/ou o dicionário.
5. O programa deve usar **if/else** para validar entradas do usuário e tomar decisões.
'''

alunos = {}
menu = {
  1: 'Adicionar aluno e suas notas',
  2: 'Listar todos os alunos e suas notas',
  3: 'Mostrar a média de um aluno específico',
  4: 'Sair'
}

def adicionar_aluno():
  notas = []
  nome = input('Digite o nome do aluno: ')

  try:
    for n in range(1, 4):
      nota = int(input(f'Digite a {n}ª nota (0 a 10): '))

      if nota < 0 or nota > 10:
        print('Valor da nota não permitido, voltando para o menu.')
        return
      else:
        notas.append(nota)

  except ValueError:
    print('Nota digitada invalida, voltando para o menu.')
    return
  
  alunos[nome] = notas
  print('Aluno(a) cadastrado com sucesso.')



def listar_alunos():
  if not alunos:
    print('Nenhum aluno(a) cadastrado.')
  else:
    for aluno, notas in alunos.items():
      print(f'{aluno} | Notas: {notas}')

def mostrar_media(nome):
  notas = alunos.get(nome)
  media = sum(notas) / len(notas)
  print(f'Aluno: {nome} | Notas: {alunos.get(nome)} | Média: {media:.2f}')



while True:
  print('----- MENU -----')
  for opcao, descricao in menu.items():
    print(f'{opcao} - {descricao}')

  try:
    opcao = int(input('Selecione: '))

    if opcao == 1:
      adicionar_aluno()
    
    elif opcao == 2:
      listar_alunos()
    
    elif opcao == 3:
      nome = input('Digite o nome do aluno que deseja ver a média: ')

      if nome in alunos:
        mostrar_media(nome)
      else:
        print('Aluno(a) não localizado(a).')
        print('Retornando ao menu')
    
    elif opcao == 4:
      print('Saindo...')
      break
    
    else:
      print('Digite uma opção valida')

  except:
    print('Digite apenas números.')