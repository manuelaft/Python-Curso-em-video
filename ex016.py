# ex016

'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import trunc
num=float(input('Digite um valor: '))
print('O valor digitado, {} e a sua porção inteira é {}'.format(num,trunc(num)))

# Sem utilizar nenhuma biblioteca também tem como fazer esse exercício:

n=float(input('Digite um número: '))
print('O número digitado foi {} e sua parte inteira é {}'.format(n,int(n)))
