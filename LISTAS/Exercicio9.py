'''
Dada a lista de palavras:

palavras = ["python", "compreensao", "list", "programacao"]

Crie **uma única list comprehension** que gere uma lista com **todas as vogais** presentes em todas as palavras.
'''

palavras = ["python", "compreensao", "list", "programacao"]

vogais = [letra for palavra in palavras for letra in palavra if letra in 'aeiou']

print(vogais)