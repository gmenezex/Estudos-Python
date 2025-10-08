'''
Usuário deve informar a quantidade de **kWh consumida** em sua casa no mês.
O programa deve calcular o valor da conta de energia conforme as regras:
- Até **100 kWh** → R$ 0,50 por kWh
- De **101 a 200 kWh** → R$ 0,70 por kWh
- Acima de **200 kWh** → R$ 0,90 por kWh

No final, o programa deve mostrar:
- O consumo informado
- O valor total da conta
'''

qtd_kwh = float(input('Digite a quantidade de kWh consumida: '))
valor_conta = 0.00

if qtd_kwh <= 100:
    valor_conta = qtd_kwh * 0.50
    print('Consumo menor ou igual a 100')
elif qtd_kwh <= 200:
    valor_conta = qtd_kwh * 0.70
    print('Consumo entre 101 a 200')
else:
    valor_conta = qtd_kwh * 0.90
    print('Consumo acima de 200')

valor_conta = round(valor_conta, 2)
print('Consumo informado: ', qtd_kwh)
print('Valor total da conta: R$', valor_conta)
