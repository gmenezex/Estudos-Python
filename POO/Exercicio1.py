'''
### Descrição

Crie uma classe chamada `Aluno` que deve conter:

1. **Atributos**:
    - `nome`
    - `idade`
    - `nota`
2. **Métodos**:
    - `mostrar_informacoes()` → mostra todos os dados do aluno.
    - `aprovado()` → retorna **"Aprovado"** se a nota for maior ou igual a 7, senão **"Reprovado"**.
'''

class Aluno:
  def __init__(self, nome, idade, nota):
    self.nome = nome
    self.idade = idade
    self.nota = nota
  
  def mostrar_informacoes(self):
    return f'{self.nome} | Idade: {self.idade} | Nota: {self.nota}'
  
  def aprovado(self):
    if self.nota >= 7:
      return f'Aluno: {self.nome} - Aprovado'
    else:
      return f'Aluno: {self.nome} - Reprovado'

aluno1 = Aluno('Gabriel', 27, 6)
aluno2 = Aluno('Evelyn', 26, 9)

print(aluno1.mostrar_informacoes())
print(aluno2.mostrar_informacoes())
print('-'*20)
print(aluno1.aprovado())
print(aluno2.aprovado())