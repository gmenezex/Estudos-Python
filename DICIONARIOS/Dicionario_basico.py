pessoa = {
  'nome': 'Gabriel',
  'idade': 27,
  'Profissao': 'Futuro desenvolvedor backend',
  'CHN': 'Sim'
}

print(pessoa.items())

del pessoa['CHN']

pessoa['linguagens'] = ['Python', 'SQL', 'Javascript']
print(pessoa.items())
print(pessoa.get('linguagens')[1])

pessoa['pet'] = {'nome': 'Lili', 'idade': 7, 'peso': '9kg'}
print(pessoa.items())

print(pessoa.get('pet').get('nome'))