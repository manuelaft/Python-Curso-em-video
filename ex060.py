# ex060

''' Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

import math
num=int(input('Digite um número para\nCalcular seu fatorial: '))
print(f'Calculando {num}! = ',end='')
for c in range (num,1,-1):
    print(c,end=' x ')
print(f'1 = {math.factorial(num)}')
