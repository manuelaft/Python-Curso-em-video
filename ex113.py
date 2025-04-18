# ex113

'''Reescreva a função leiaInt() do ex104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

from colorama import Fore, init
init(autoreset=True)
def leiaInt(num):
    while True:
        try:
            a=int(input(num))
        except (ValueError, TypeError):
            print(Fore.RED + 'ERRO: Por favor digite um número inteiro válido')
        except KeyboardInterrupt:
            print(Fore.RED + 'O usuário preferiu não informar um valor ')
            return 0
            break
        else:
            return a
            break
def leiaFloat(real):
    while True:
        try:
            b=float(input(real))
        except (ValueError,TypeError):
            print(Fore.RED + 'ERRO: Por favor digite um número inteiro válido')
        except KeyboardInterrupt:
            print(Fore.RED + 'O usuário preferiu não informar um valor')
            return 0
            break
        else:
            return b
            break
while True:
    print('=-'*30)
    num=leiaInt('Digite um inteiro: ')
    real=leiaFloat('Digite um real: ')
    print(f'O valor inteiro digitado foi {num} e o valor real foi {real}')
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta not in 'SN':
        print(Fore.RED + 'ERRO! Por favor digite apenas S ou N.')
    if resposta=='N':
        break
print('=-'*30)
print('>> ENCERRADO <<')

# 'continue' dentro de um laço joga pra o início do loop de novo
