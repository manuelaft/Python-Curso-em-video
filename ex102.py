# ex102

'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular 
e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(i,show=False):
    from time import sleep
    fat=1
    for c in range(i,0,-1):
        if show:
            fat=fat*c
            print(f'{c}',end=' ',flush=True)
            sleep(0.5)
            if c>1:
                print('x',end=' ')
            else:
                print('=',end=' ')
        else:
            fat=fat*c
    return fat

# Programa Principal
print('=-'*15)
print(f'{'FATORIAL DE UM NÚMERO':^30}')
print('=-'*15)
while True:
    num=int(input('Deseja ver o fatorial de qual número? '))
    print(fatorial(num,show=False))
    calculo=' '
    while calculo not in 'SN':
        calculo=str(input('Deseja ver o cálculo detalhado? [S/N] ')).upper().split()[0]
        if calculo not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
    if calculo=='S':
        print(fatorial(num,show=True))
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Quer continuar? [S/N] ')).upper().split()[0]
        if resposta not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
    if resposta=='N':
        break
print('>> ENCERRADO <<')
