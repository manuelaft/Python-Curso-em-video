# ex096

'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(a,b):
    a=a*b
    print(f'A área de um terreno {l} x {c} é de {a:.2f}m^2\n')

print()
print(' Controle de Terreno')
print('-'*21)
l=float(input('LARGURA (m): '))
c=float(input('COMPRIMENTO (m): '))
area(l,c)
