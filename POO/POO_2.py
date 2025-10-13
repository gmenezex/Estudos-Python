class Carro:
  #Atributos (propriedades)
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.ligado = False
  
  #Métodos
  def ligar(self):
    self.ligado = True
    print(f'{self.modelo} está ligado!')
  
  def desligar(self):
    self.ligado = False
    print(f'{self.modelo} está desligado!')
  

carro1 = Carro('Toyota', 'Corolla', 2024)

print(carro1.modelo)
carro1.ligar()
carro1.desligar()