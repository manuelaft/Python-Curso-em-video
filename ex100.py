# ex100

'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep
def somaPar(*numeros):
    pares=[]
    for valor in numeros:
        if valor%2==0:
            pares.append(valor)
    print(sum(pares))
lista=[]
print(f'Sorteando 5 valores da lista:',end=' ')
for c in range(0,5):
    lista.append(randint(1,20))
    print(f'{lista[c]}',end=' ',flush=True)
    sleep(0.5)
print('PRONTO!')
print(f'Somando os valores pares de {lista}, temos ',end='',flush=True)
sleep(1)
somaPar(*lista)
