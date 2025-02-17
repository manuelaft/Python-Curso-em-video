# ex075

'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

print('=-'*20)
pares=[]
n1=int(input('Digite um número: '))
if n1%2==0:
    pares.append(n1)
n2=int(input('Digite o segundo valor: '))
if n2%2==0:
    pares.append(n2)
n3=int(input('Digite o terceiro valor: '))
if n3%2==0:
    pares.append(n3)
n4=int(input('Digite o último valor: '))
if n4%2==0:
    pares.append(n4)
tupla=n1,n2,n3,n4
print(f'Você digitou os valores: {n1}, {n2}, {n3}, {n4}')
if tupla.count(9)==1:
    vezes='vez'
else:
    vezes='vezes'
print(f'O valor 9 apareceu {tupla.count(9)} {vezes}')

if 3 not in tupla:
    valor3='não apareceu em nenhuma posição'
else:
    valor3=(f'apareceu na {(tupla.index(3))+1}ª posição')
print(f'O valor 3 {valor3}')

print(f'Os valores pares digitados foram: {pares}')
print('=-'*20)
