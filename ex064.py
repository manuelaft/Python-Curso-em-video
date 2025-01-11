# ex064

'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

c=0
num=0
lista=[] # a lista vazia precisa ser criada antes pq senão a cada loop ia criar uma lista NOVA, não atualizar os valores (print --> 999)
while num!=999:
    num=int(input('Digite um número [999 para parar]: '))
    c+=1
    lista.append(num)
soma=sum(lista)
print('Você digitou {} números e a soma entre eles foi {}'.format(c-1,soma-999))
