'''
Função com retorno e passagem de parametros
'''
def somar(a, b):
  return a + b

resultado = somar(5, 6)
print(resultado)


def valida_usuario(usuario, senha):
  if usuario == 'Gabriel' and senha == 'python':
    return 'Usuario logado com sucesso!'

  return 'Nome do usuario ou senha incorretos.'

logar = valida_usuario('Joao', 1234)
print(logar)

logar = valida_usuario('Gabriel', 'python')
print(logar)