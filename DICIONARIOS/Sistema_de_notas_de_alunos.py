'''
Crie um programa que:

1. Peça ao usuário para informar o nome de **3 alunos** e suas respectivas **notas** (de 0 a 10).
2. Guarde essas informações em um **dicionário**, onde a chave é o nome do aluno e o valor é a nota.
3. Após cadastrar, mostre:
    - Todos os alunos e suas notas.
    - A **média** da turma.
    - O **aluno com a maior nota**.
    - O **aluno com a menor nota**.
'''
alunos = {}

for _ in range(3):
  nome = input('Digite o nome do aluno: ')
  nota = int(input('Digite a nota do aluno: '))
  alunos[nome] = nota

media = 0
maior_aluno = None
menor_aluno = None

for aluno, nota in alunos.items():
  print(f'{aluno} : {nota}')

  if maior_aluno is None or nota > alunos[maior_aluno]:
    maior_aluno = aluno

  if menor_aluno is None or nota < alunos[menor_aluno]:
    menor_aluno = aluno

  media += nota

media /= len(alunos)
print(f'Média: {media:.2f}')
print(maior_aluno, alunos[maior_aluno])
print(menor_aluno, alunos[menor_aluno])