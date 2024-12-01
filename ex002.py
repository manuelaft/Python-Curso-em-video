nome=input(f'{'\033[m'}Qual o seu nome? ')
print('Seja muito bem vido à nossa comunidade {}{}{}!'.format('\033[32m',nome,'\033[m'))

n1=int(input('Digite um número: '))
n2=int(input('Digite o segundo número: '))
print(f'A soma entre eles é {'\033[34m'}{n1+n2}{'\033[m'}')

# ou, melhor:

num1=int(input('Digite um número: '))
num2=int(input('Digite o segundo número: '))
s=num1+num2
print('A soma entre eles é {}{}{}, correto?'.format('\033[35m',s,'\033[m'))

#Teste 02

num=input('Digite um valor: ')
print(type(num))

#Teste 03

num1=int(input('Digite um valor: '))
num2=int(input('Digite o segundo valor: '))
s=num1+num2
print('A soma entre os números {}{}{} e {}{}{} vale {}{}{}'.format('\033[33m',num1,'\033[m','\033[35m',num2,'\033[m','\033[31m',s,'\033[m'))

# ou, de um jeito melhor:

n1=float(input('Digite um número: '))
n2=float(input('Digite um segundo número: '))
s=n1+n2
print('A soma entre os números {}{}{} e {}{}{} vale {}{}{}'.format('\033[34m',n1,'\033[m','\033[36m',n2,'\033[m','\033[33m',s,'\033[m'))
