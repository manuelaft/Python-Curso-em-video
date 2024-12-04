# ex033

'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

num1=int(input('Primeiro valor: '))
num2=int(input('Segundo valor: '))
num3=int(input('Terceiro valor: '))
lista=[num1,num2,num3]
print('O menor valor digitado foi: {}'.format(min(lista)))
print('O maior valor digitado foi: {}'.format(max(lista)))

# ver do Guanabara utilizando condições simples

num1=int(input('Primeiro valor: '))
num2=int(input('Segundo valor: '))
num3=int(input('Terceiro valor: '))
if num1>num2>num3 or num1>num3>num2:
    maior=num1
if num2>num1>num3 or num2>num3>num1:
    maior=num2
if num3>num1>num2 or num3>num2>num1:
    maior=num3
print(f'O maior valor digitado foi {maior}')

if num1<num2<num3 or num1<num3<num2:
    menor=num1
if num2<num1<num3 or num2<num3<num1:
    menor=num2
if num3<num2<num1 or num3<num1<num2:
    menor=num3
print(f'O menor valor digitado foi {menor}')
