#ex005

'''Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'''

n=int(input('Digite um valor qualquer: '))
s=n+1
a=n-1
print('O número antecessor do número {} é {}{}{}, e o seu sucessor é {}{}{}'.format(n,'\033[33m',a,'\033[m','\033[33m',s,'\033[m'))

# utilizando uma variável:

n=int(input('Digite um valor qualquer: '))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor {}'.format(n,(n-1),(n+1)))
