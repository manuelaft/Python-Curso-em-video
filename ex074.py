# ex074

'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint as rd
print('=-'*20)
tupla=rd(0,10),rd(0,10),rd(0,10),rd(0,10),rd(0,10)
print(f'Os valores sorteados foram: {tupla[0]} {tupla[1]} {tupla[2]} {tupla[3]} {tupla[4]}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
print('=-'*20)
