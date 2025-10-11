'''
### Nomes filtrados

nomes = ["ana", "joao", "maria", "carlos", "matheus"]

A partir da lista de nomes acima, gere outra lista apenas com os nomes que começam com a letra `"m"`.
'''

nomes = ["ana", "joao", "maria", "carlos", "matheus"]

nomes_com_m = [nome for nome in nomes if nome[0] == 'm']
print(nomes_com_m)