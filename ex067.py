# ex067

'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''

cont=0
while True:
    num=int(input('Quer ver a tabuada de qual valor? '))
    print('='*40)
    if '-' in str(num):
        nada=0
    else:
        for c in range (0,10):
            cont+=1
            print(f'{num} x {cont} = {num*cont}')
            if cont>=10:
                cont=0
    if '-' in str(num):
        break
    print('='*40)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')

# ver do Guanabara

'''while True:
        num=int(input('Digite o número: '))
        if num<0:
            break
        else:
            for c in range(0,10): '''