class Veiculo:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
  
  def mostrar_info(self):
    return f'{self.marca} | {self.modelo} | {self.ano}'

# Classe Carro está herando todos os atributos e métodos de Veiculo
class Carro(Veiculo):
  def __init__(self, marca, modelo, ano, portas):
    super().__init__(marca, modelo, ano) # > Aqui estamos utilizando os mesmos atributos de veiculo
    self.portas = portas # > Tem seu proprio atributo
  
  def mostrar_info(self):
    return f'{super().mostrar_info()} | Portas: {self.portas}'

class Moto(Veiculo):
  def __init__(self, marca, modelo, ano, cilindradas):
    super().__init__(marca, modelo, ano)
    self.cilindradas = cilindradas

  def mostrar_info(self):
    return f'{super().mostrar_info()} | Cilindradas: {self.cilindradas}'

carro1 = Carro('Toyota', 'Corolla', 2024, 4)
moto1 = Moto('Honda', 'CB500', 2022, 500)

print(carro1.mostrar_info())
print(moto1.mostrar_info())