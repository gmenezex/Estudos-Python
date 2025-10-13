'''
# Conta Bancária

### Objetivo

Criar uma classe `ContaBancaria` que vai evoluir aos poucos com **atributos, métodos, encapsulamento e herança**.

---

## **Etapa 1 – Classe simples**

Crie uma classe `ContaBancaria` com os atributos:

- titular (nome do dono da conta)
- saldo (começa em 0)

E um método para mostrar as informações da conta.

---

## **Etapa 2 – Depósito e Saque**

Adicione métodos para:

- `depositar(valor)`
- `sacar(valor)` (verificando se tem saldo suficiente).

---

## **Etapa 3 – Encapsulamento**

Proteja o saldo (`__saldo`) para não ser acessado diretamente.

Crie um método `ver_saldo()` para consultar.

---

## **Etapa 4 – Herança**

Crie uma classe `ContaPoupanca` que herda de `ContaBancaria`, mas adiciona:

- método `render_juros(taxa)` que aumenta o saldo de acordo com a taxa.

---
'''

class ContaBancaria:
  def __init__(self, titular):
    self.titular = titular
    self.__saldo = 0
  
  def ver_saldo(self):
    return self.__saldo

  def mostrar_dados(self):
    print(f'Titular: {self.titular} | Saldo: R$ {self.ver_saldo():.2f}')
  
  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
      print(f'Deposito de R$ {valor:.2f} realizado com sucesso!')
    else:
      print('Valor inválido')
  
  def sacar(self, valor):
    if self.__saldo >= valor:
      self.__saldo -= valor
      print(f'Saque de R$ {valor:.2f} realizado com sucesso')
    else:
      print('Saldo insuficiente para o saque')


conta1 = ContaBancaria('Gabriel')
conta1.depositar(500)
conta1.sacar(100)
conta1.mostrar_dados()

class ContaPoupanca(ContaBancaria):
  def render_juros(self, taxa):
    rendimento = self.ver_saldo() * taxa / 100
    self.depositar(rendimento)
    print(f'Juros de R$ {rendimento:.2f} aplicados.')


conta2 = ContaPoupanca('Evelyn')
conta2.mostrar_dados()
conta2.depositar(200)
conta2.render_juros(5)
conta2.mostrar_dados()