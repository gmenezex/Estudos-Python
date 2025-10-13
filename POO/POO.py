class Celular:
  #Propriedades
  marca = 'Nokia'
  modelo = 'Tijolão'
  cor = 'Azul'
  tem_camera = False
  bateria = 'Infinita'

  #Métodos (Funções) (self é o primeiro parametro e é obrigatorio.)
  def fazer_ligacao(self):
    print('Fazendo ligação...')
  
  def jogar_cobrinha(self):
    print('Jogando cobrinha...')

  def despertador(self):
    print('Despertando...')
  
  def calcular(self, v1, v2):
    return v1 + v2

# Instancia da classe celular. Essa variavel viru um "celular" e assim possui seus atributos e métodos(funções)
celular = Celular()
print(celular.modelo)
print(celular.bateria)

celular.fazer_ligacao()
print(celular.calcular(10, 20))