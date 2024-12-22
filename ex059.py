# ex059

'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep as s
n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
print('   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa') # ou 3 aspas
usuario=int(input('>>>>>> Qual é a sua opção? '))
while usuario!=5:
    if usuario==1:
        print('A soma entre {} + {} é {}'.format(n1,n2,n1+n2))
        print('=-'*15), s(3)
        print('   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa')
        usuario=int(input('>>>>>> Qual é a sua opção? '))
    if usuario==2:
        print('O resultado de {} x {} é {}'.format(n1,n2,n1*n2))
        print('=-'*15), s(3)
        print('   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa')
        usuario=int(input('>>>>>> Qual é a sua opção? '))
    if usuario ==3:
        print(f'Entre {n1} e {n2}, o maior valor é {max(n1,n2)}')
        print('=-'*15), s(3)
        print('   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa')
        usuario=int(input('>>>>>> Qual é a sua opção? '))
    if usuario==4:
        n1=int(input(('Informe os números novamente:\nPrimeiro valor: ')))
        n2=int(input('Segundo valor: '))
        print('=-'*15), s(3)
        print('   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa')
        usuario=int(input('>>>>>> Qual é a sua opção? '))
    if usuario>5:
        print('Opção Invállida. Tente novamente')
        print('=-'*15), s(3)
        print('   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa')
        usuario=int(input('>>>>>> Qual é a sua opção? '))
print('Finalizando...')
print('=-'*15), s(3)
print('Fim do programa! Volte sempre!')
