# ex088

'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados 
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import sample as s
from time import sleep
print('='*40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('='*40)
quantidade=int(input('Quantos jogos você quer que eu sorteie? '))
print('=-'*5,end=' ')
print(f'SORTEANDO {quantidade} JOGOS',end=' ')
print('=-'*5)
for contador in range(quantidade):
    lista=s(range(0,61),6) # O random.sample já cria uma lista por si só, é usado para randomizar x números em um range, sem repetir!
    lista.sort()
    print(f'Jogo {contador+1}: {lista}')
    sleep(2)
print('=-'*6,end=' ')
print('< BOA SORTE! >',end=' ')
print('=-'*6)
