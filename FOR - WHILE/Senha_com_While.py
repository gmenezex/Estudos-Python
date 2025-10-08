'''
Crie um programa que peça a senha do usuário.
A senha correta é `"python123"`.
O programa só deve parar quando o usuário acertar a senha.
No final, exiba quantas tentativas foram necessárias.
'''

tentativas = 0

while True:
    senha = input('Digite a senha: ')
    tentativas += 1
    if senha == 'python123':
        break
    print('Senha incorreta!')

print(f'Senha correta! Você acertou em {tentativas} tentativas.')
