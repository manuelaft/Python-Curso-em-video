# ex080

'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista=[]
print('=-'*30)
for c in range(0,5):
    n=int(input(f'Digite um valor para a posição {c}: '))
    if c==0:
        lista.append(n)
        print('Valor adicionado ao final da lista')

    elif c==1:
        if n<lista[0]:
            lista.insert(0,n)
            print('Valor adicionado à posição 0 da lista')
        else:
            lista.append(n)
            print('Valor adicionado ao final da lista')

    elif c==2:
        if n>=lista[1]:
            lista.append(n)
            print('Valor adicionado ao final da lista')
        elif n<lista[0]:
            lista.insert(0,n)
            print('Valor adicionado à posição 0 da lista')
        else:
            lista.insert(1,n)
            print('Valor adicionado na posição 1 da lista')

    elif c==3:
        if n>=lista[2]:
            lista.append(n)
            print('Valor adicionado ao final da lista')
        elif n<lista[0]:
            lista.insert(0,n)
            print('Valor adicionado à posição 0 da lista')
        elif n<lista[1]:
            lista.insert(1,n)
            print('Valor adicionado na posição 1 da lista ')
        else:
            lista.insert(2,n)
            print('Valor adicionado na posição 2 da lista')

    elif c==4:
        if n>=lista[3]:
            lista.append(n)
            print('Valor adicionado ao final da lista')
        elif n<lista[0]:
            lista.insert(0,n)
            print('Valor adicionado à posição 0 da lista')
        elif n<lista[1]:
            lista.insert(1,n)
            print('Valor adicionado na posição 1 da lista')
        elif n<lista[2]:
            lista.insert(2,n)
            print('Valor adicionado na posição 2 da lista')
        else:
            lista.insert(3,n)
            print('Valor adicionado na posição 3 da lista')
print('=-'*30)
print(f'Os valores digitados em ordem foram {lista}')