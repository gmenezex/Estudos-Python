'''
### Nomes em maiúsculas

Dada a lista `nomes = ["ana", "joao", "maria", "carlos"]`, crie uma nova lista com todos os nomes em maiúsculas.
'''
nomes = ["ana", "joao", "maria", "carlos"]

nomes_maisculos = [nome.upper() for nome in nomes]
print(nomes_maisculos)