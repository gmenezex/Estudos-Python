'''
Peça ao usuário para digitar a **idade** e informe a situação do voto no Brasil:
- Menor que **16 anos** → **Não vota**
- Entre **16 e 17 anos** OU **maior que 70 anos** → **Voto facultativo**
- Entre **18 e 70 anos** → **Voto obrigatório**
'''

idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Não vota')
elif (idade >= 16 and idade < 18) or idade > 70:
    print('Voto facultaivo')
else:
    print('Voto obrigatório')
