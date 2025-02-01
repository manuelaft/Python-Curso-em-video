# ex065

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

continuação='s'

contador=0 # quantidade de números digitados

lista=[] # somar e fazer média de todos os num digitados

while continuação =='s'or continuação=='S': # while continuação in 'Ss':
    num=int(input('Digite um número: '))
    contador+=1
    lista.append(num)
    
    continuação=str(input('Quer continuar ou não? [S/N] ')).strip()[0]

print(f'Você digitou {contador} números e a média foi {sum(lista)/contador}')
print(f'O maior valor foi {max(lista)} e o menor valor foi {min(lista)}')
