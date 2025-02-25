# ex082

'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares 
e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista=[]
pares=[]
ímpares=[]
while True:
    n=int(input('Digite um número: '))
    lista.append(n)
    if n%2==0:
        pares.append(n)
    else:
        ímpares.append(n)
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N] ')).upper().strip() [0]
    if resp in 'N':
        break
print('=-'*30)
print(f'A lista completa é {lista}')
pares.sort
print(f'A lista dos números pares é {pares}')
ímpares.sort
print(f'A lista dos números ímpares é {ímpares}')

# também tem como fazer utilizando for in enumerate
