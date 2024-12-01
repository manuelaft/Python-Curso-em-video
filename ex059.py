n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
print('   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa')
usuario=int(input('>>>>>> Qual é a sua opção? '))
while usuario!=5:
    if usuario==1:
        print('A soma entre {} + {} é {}'.format(n1,n2,n1+n2))
        print('=-'*15)
        print('   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa')
        usuario=int(input('>>>>>> Qual é a sua opção? '))
    if usuario==2:
        print('O resultado de {} x {} é {}'.format(n1,n2,n1*n2))


