class Animal:
  def emitir_som(self):
    print('Qualquer som...')

class Cachorro(Animal):
  # Aqui estamos alterando o método emitir_som da classe Animal
  def emitir_som(self):
    print('Au Au Au !')

class Gato(Animal):
  def emitir_som(self):
    print('Miauuuu !')

cachorro = Cachorro()
gato = Gato()

cachorro.emitir_som()
gato.emitir_som()