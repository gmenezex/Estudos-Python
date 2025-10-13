'''
### Exercício: Sistema de Biblioteca
Crie um programa orientado a objetos para gerenciar uma **biblioteca**.

### Regras:
1. Crie uma classe **Livro** com os atributos:
    - `titulo`
    - `autor`
    - `ano`
    - `disponivel` (booleano, começa como `True`)
    
    E métodos:
    
    - `emprestar()` → muda o estado para `False` se o livro estiver disponível.
    - `devolver()` → muda o estado para `True`.
    - `__str__()` → retorna uma string com título, autor e status do livro.
2. Crie uma classe **Usuario** com os atributos:
    - `nome`
    - `livros_emprestados` (lista)
    
    E métodos:
    
    - `emprestar_livro(livro)` → adiciona o livro à lista do usuário se estiver disponível.
    - `devolver_livro(livro)` → remove da lista e devolve para a biblioteca.
3. Crie uma classe **Biblioteca** que armazene todos os livros em uma lista.
    - Métodos:
        - `adicionar_livro(livro)`
        - `listar_livros()` (mostra todos com status de disponibilidade)
        - `buscar_livro(titulo)` (retorna o livro se existir)
'''

class Livro:
  def __init__(self, titulo, autor, ano):
    self.titulo = titulo
    self.autor = autor
    self.ano = ano
    self.disponivel = True

  def emprestar(self):
    if self.disponivel == True:
      self.disponivel = False
      print(f'{self.titulo} - foi emprestado')
    else:
      print(f'Livro não está disponível')
  
  def devolver(self):
    self.disponivel = True
    print(f'{self.titulo} - Devolvido')
  
  def __str__(self):
    return f'Titulo: {self.titulo} | Autor: {self.autor} | Status: {"Disponível" if self.disponivel else "Indisponível"} '
  
class Usuario:
  def __init__(self, nome):
    self.nome = nome
    self.livros_emprestados = []
  
  def emprestar_livro(self,livro):
    if livro.disponivel:
      livro.emprestar()
      self.livros_emprestados.append(livro)
    else:
      livro.emprestar()
  
  def devolver_livro(self, livro):
    if livro in self.livros_emprestados:
      livro.devolver()
      self.livros_emprestados.remove(livro)
    else:
      print(f'{self.nome} não possui o livro "{self.titulo}"')

class Biblioteca:
  def __init__(self):
    self.livros = []
  
  def adicionar_livro(self, livro):
    self.livros.append(livro)
  
  def listar_livros(self):
    for livro in self.livros:
      print(livro)
    print("-----------------------------")
  
  def buscar_livro(self, titulo):
    for livro in self.livros:
      if livro.titulo.lower() == titulo.lower():
        return f'Encontrado: {livro}'
    print(f'Livro "{titulo}" não encontrado.')

biblioteca = Biblioteca()
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro('O Homem Mais Rico da Babilônia','George S. Clason', 1926)
livro3 = Livro("O Cortiço", "Aluísio Azevedo", 1890)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()

gabriel = Usuario('Gabriel')
gabriel.emprestar_livro(livro1)
gabriel.emprestar_livro(livro2)
gabriel.emprestar_livro(livro1)

biblioteca.listar_livros()
gabriel.devolver_livro(livro1)
biblioteca.listar_livros()

print(biblioteca.buscar_livro('Dom Casmurr'))
print(biblioteca.buscar_livro('Dom Casmurro'))
