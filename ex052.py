# ex052

'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

from colorama import Fore,init
init()
lista=0
num=int(input('Digite um número: '))
for c in range(1,num+1):
    if num%c==0:
        lista+=num%c==0
        print(Fore.YELLOW, end=' ')
        print(c, end=' ')
    else:
        print(Fore.RED,end=' ')
        print(c, end=' ')               
print(Fore.RESET + '\nO número {} foi divisível {} vezes'.format(num,lista))
if lista==2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
