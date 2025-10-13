class Pet:
  def __init__(self, nome, peso):
    self.nome = nome
    self.peso = peso
  
  def imprimirPet(self):
    print(f'Nome do pet: {self.nome}')
    print(f'Peso do pet: {self.peso}')
  
  def alimentarPet(self, comida):
    self.peso += comida
  

class Abrigo:
  # catalogo = [] > Publico - Pode ser acessado sempre
  # _catalogo = [] > Protegido - Pode ser acessado pela sua classe e suas heranças
  # __catalogo = [] > Privado - Só a própria classe pode acessar.
  __catalogo = []

  def adicionarPet(self, pet):
    self.__catalogo.append(pet)
  
  def imprimirAbrigo(self):
    print('Pets no abrigo:')
    print('-' * 20)
    for pet in self.__catalogo:
      pet.imprimirPet()
      print('-' * 20)


abrigo = Abrigo()

pet = Pet('Duque', 5)
pet.alimentarPet(1)
abrigo.adicionarPet(pet)


pet = Pet('Lili', 9)
pet.alimentarPet(1)
abrigo.adicionarPet(pet)

abrigo.imprimirAbrigo()
