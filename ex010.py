#ex010

'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

print('_'*7,'CONVERSOR DE MOEDAS','_'*7)
r=float(input('Quantos reais você tem na sua carteira agora mesmo? R$'))
d=r/5.12 #valor do dólar atualmente
print('Você tem {:.2f} dólares US$.'.format(d))

# atividade complementar (euros e won)

real=float(input('Quantos reais você tem na carteira? R$'))
print('Você tem {:.2f} US$ (dólar)\n{:.2f} euros\n{:.2f} won'.format(real/5.12,real/5.48,real*269.32))
