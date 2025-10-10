'''
Peça nomes de alunos e suas 3 notas.

Depois calcule a média de cada um.
'''

alunos = {}

for _ in range(3):
  nome = input('Digite o nome do aluno: ')
  notas = []
  for n in range(1, 4):
    nota = int(input(f'Informe a {n}ª nota: '))
    notas.append(nota)
  alunos[nome] = notas

for aluno, notas in alunos.items():
  media = sum(notas) / len(notas)
  print(f'Aluno(a): {aluno} | Média: {media}')