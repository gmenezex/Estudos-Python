'''
Escreva um programa em Python que:

1. Peça ao usuário para digitar as **notas de 5 alunos** (valores de 0 a 10).
2. Armazene todas as notas em uma lista.
3. Mostre na tela:
    - A lista completa de notas.
    - A **maior** e a **menor** nota.
    - A **média da turma**.
    - Todas as notas **acima da média**.
    - Quantos alunos **ficaram abaixo de 7**.
'''

notas = []
media = 0
acima_media = []
abaixo_media = 0

for i in range(1, 6):
  nota = int(input(f'Digite a {i}ª nota: '))
  notas.append(nota)

maior = notas[0]
menor = notas[0]

for nota in notas:
  media += nota
  if nota > maior:
    maior = nota
  if nota < menor:
    menor = nota

media /= len(notas)

for nota in notas:
  if nota > media:
    acima_media.append(nota)
  else:
    abaixo_media += 1


print(f'Notas: {notas}')
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Média da turma: {media}')
print(f'Notas cima da média: {acima_media}')
print(f'Alunos abaixo de {media}: {abaixo_media}')
