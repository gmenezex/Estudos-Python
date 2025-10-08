'''
Peça ao usuário para digitar 3 notas, o sistema ira calcular e apresentar na tela a média:
- Maior ou igual a 7 → ** Situação: Aprovado **
- Maior ou igual a 5 e menor que 7 → ** Situação: Recuperação **
- Menor que 5 → ** Situação: Reprovado **
'''

nota_1 = float(input('Nota da prova 1: '))
nota_2 = float(input('Nota da prova 2: '))
nota_3 = float(input('Nota da prova 3: '))

media = (nota_1 + nota_2 + nota_3) / 3
media = round(media, 2)

print('Média do aluno: ', media)

if media >= 7:
    print('Situação: Aprovado')
elif media >= 5:
    print('Situação: Recuperação')
else:
    print('Situação: Reprovado')
