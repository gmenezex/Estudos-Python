'''
### Palavras com mais de 4 letras

Dada a lista:

palavras = ["casa", "aviao", "sol", "computador", "lua", "carro"]


Crie uma nova lista apenas com as palavras que têm **mais de 4 letras**.
'''

palavras = ["casa", "aviao", "sol", "computador", "lua", "carro"]

novas_palavras = [palavra for palavra in palavras if len(palavra) > 4]
print(novas_palavras)