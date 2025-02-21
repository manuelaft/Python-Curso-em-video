# ex078

'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''

lista=[]
maior=menor=0
for c in range (0,5):
    lista.append(int(input(f'Digite um número para a posição {c}: ' )))

print(f'Você digitou {lista}')
print(f'O maior número digitado foi {max(lista)} na posição',end=' ')
for indice,valor in enumerate(lista):
    if valor==max(lista):
        print(f'{indice}...',end='')
print(f'\nO menor valor digitado foi {min(lista)} para a posição',end=' ')
for indice,valor in enumerate(lista):
    if valor==min(lista):
        print(f'{indice}...',end='')

# versão sem usar min ou max

'''menor=maior=0
.
.
lista.append(...)

if c==0:

    maior=menor=lista[c]

else:
    if lista[c]>maior:
    
        maior=lista[c]
    
    if lista[c]<menor:
        
        menor=lista[c]






'''