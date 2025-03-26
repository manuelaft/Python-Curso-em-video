# ex089

'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

lista=[]
print('=-'*20)
while True:
    nome=str(input('Nome: ')).capitalize()
    n1=float(input('Nota 1: '))
    n2=float(input('Nota 2: '))
    media=(n1+n2)/2

    lista.append([nome,[n1,n2],media])

    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break

print('=-'*20)
print(f'{'No.':<5}',end='')
print(f'{'NOME':<10}',end='')
print(f'{'MÉDIA':<10}')
print('=-'*20)

for c in range(len(lista)):
    print(f'{c:<5}',end='')
    print(f'{lista[c][0]:<10}',end='')
    print(f'{lista[c][2]:>5}')

print('=-'*20)
notas=0
while True:
    notas=int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if notas==999:
        break
    print(f'Notas de {lista[notas][0]} são {lista[notas][1]}')
    print('=-'*10)
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')

