# ex099

'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep
def maior(*num):
    print('=-'*20)
    print(f'Analisando os valores passados...')
    sleep(1)
    for c in range(0,len(num)):
        print(f'{num[c]}',end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')
    print('=-'*20)

lista=[]
quantidade=int(input('Quantos valores você quer digitar? '))
for c in range(0,quantidade):
    lista.append(int(input('Digite o valor: ')))
    
maior(*lista)
