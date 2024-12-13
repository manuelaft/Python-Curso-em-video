# ex037

'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

num=int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
op=int(input('Sua opção: '))
if op == 1:
    print(f"{num} convertido para BINÁRIO é igual a",format(num,'b'))
if op == 2:
    print(f'{num} convertido para OCTAL é igual a',format(num,'o'))
if op == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a',format(num,'x'))

# Ver corrigida do Gustavo Guanabara, utilizando o fatiamento de string para retirar o 0b, 08 e 0x do py

num=int(input('Digite um número inteiro: '))
print(""" Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL""")
op=int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Desculpe, opção inválida. Tente novamente')

