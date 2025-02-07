# ex068

'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
venceu=0
while True:
    num=int(input('Diga um valor: '))
    pi=str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-'*40)
    pc=int(random.randint(0,100))
    soma=num+pc
    if soma %2==0:
        somaRESULTADO=str('DEU PAR')
    else:
        somaRESULTADO=str('DEU ÍMPAR')
    print(f'Você jogou {num} e o computador {pc}. O total foi {soma}, {somaRESULTADO}.')
    print('-'*40)
    if pi=='P'and somaRESULTADO=='DEU PAR':
        print('VOCÊ GANHOU!')
        ganhou=True
    elif pi=='P' and somaRESULTADO=='DEU ÍMPAR':
        print('VOCÊ PERDEU!')
        ganhou=False
    elif pi=='I' and somaRESULTADO=='DEU ÍMPAR':
        print('VOCÊ GANHOU!')
        ganhou=True
    elif pi=='I' and somaRESULTADO=='DEU PAR':
        print('VOCÊ PERDEU!')
        ganhou=False

    if ganhou==True:
        venceu+=1
        print('Vamos jogar novamente...')
        print('=-'*20)
    elif ganhou==False:
        break
print('=-'*20)
print(f'GAME OVER! Você venceu {venceu} vezes.')
