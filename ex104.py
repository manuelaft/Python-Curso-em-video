# ex104

'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico.'''

def LeiaInt(n):
    from colorama import init,Fore
    init(autoreset=True)
    a=input(n)
    while a.isalpha()==True or a=='':
        print(Fore.RED + 'ERRO! Digite um número inteiro válido.')
        a=input(n)
    else:
        return a

# Programa Principal
while True:
    n=LeiaInt('Digite um número: ')
    print('Você acabou de digitar o número {}'.format(n))
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Quer continuar? [S/N] ')).upper().split()[0]
        if resposta not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
    if resposta=='N':
        break
print('<< ENCERRADO >>')

# ver Guanabara !=