# ex084

'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:                                                                                                   
A) Quantas pessoas foram cadastradas.                                                                                                                
    B) Uma listagem com as pessoas mais pesadas.                                                                                                    
        C) Uma listagem com as pessoas mais leves.'''

pessoas=[]
maior_peso=0
menor_peso=float('inf')
print('=-'*30)
while True:
    nomes=str(input('Nome: '))
    pesos=int(input('Peso: '))
    pessoas.append([nomes, pesos])

    if pesos>=maior_peso:
        maior_peso=pesos

    if pesos<menor_peso:
        menor_peso=pesos
    
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break

print('=-'*30)
print('Ao todo você cadastrou {} pessoas.'.format(len(pessoas)))

print(f'O maior peso foi {maior_peso}Kg. Peso de ',end='')
for pessoa in pessoas:
    if pessoa[1]==maior_peso:
        print(pessoa[0],end=' ')

print(f'\nO menor peso foi {menor_peso}Kg. Peso de ',end='')
for pessoa in pessoas:
    if pessoa[1]==menor_peso:
        print(pessoa[0],end=' ')
