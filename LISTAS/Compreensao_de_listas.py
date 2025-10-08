numeros = [1, 2, 3, 4, 5, 6, 7]

numeros_dobrados = [numero * 2 for numero in numeros]
print(numeros)
print(numeros_dobrados)

nomes = ['Gabriel', 'Evelyn', 'Lilica', 'Ivan', 'Antonia', 'Antonio']

nomes_maisculos = [nome.upper() for nome in nomes]
print(nomes)
print(nomes_maisculos)

numeros_maiores_cinco = [n for n in numeros if n > 5]
print(numeros_maiores_cinco)

nomes_maisculos_com_a = [nome.upper() for nome in nomes if nome[0] == 'A']
print(nomes_maisculos_com_a)