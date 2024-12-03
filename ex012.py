# ex012

'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

print(' ')
print('Uma loja aplicou um desconto de 5% no valor de seu produto que originalmente custava ')
o=float(input('Digite o preço orginal do produto: R$'))
d=o*5/100
print('E agora, depois do desconto passou a custar {:.2f} reais'.format(o-d))
