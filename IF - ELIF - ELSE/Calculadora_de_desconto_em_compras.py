'''
Um cliente foi ao supermercado e comprou alguns produtos. O valor total da compra será informado pelo usuário.
O programa deve calcular o desconto e mostrar o valor final da compra de acordo com as seguintes regras:
- Se a compra for **maior ou igual a R$ 500**, o desconto é **15%**.
- Se a compra for **maior ou igual a R$ 200 e menor que R$ 500**, o desconto é **10%**.
- Se a compra for **menor que R$ 200**, o desconto é **5%**.

No final, o programa deve exibir:
- O valor total da compra.
- O valor do desconto aplicado.
- O valor final a ser pago.
'''

valor_compra = float(input('Digite o valor total da compra: R$ '))
valor_desconto = 0.00
valor_final = 0.00

if valor_compra >= 500:
    valor_desconto = valor_compra * 0.15
elif valor_compra >= 200:
    valor_desconto = valor_compra * 0.10
else:
    valor_desconto = valor_compra * 0.05

valor_final = valor_compra - valor_desconto
print('Valor total da compra: R$', valor_compra)
print('Valor do desconto aplicado: R$', valor_desconto)
print('Valor total a ser pago: R$', valor_final)
