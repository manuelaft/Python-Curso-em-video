num=int(input('Digite um número qualquer para saber sua tabuada: '))
print('='*12)
print(' {} x  1 = {}\n {} x  2 = {}\n {} x  3 = {}\n {} x  4 = {}'.format(num,num*1,num,num*2,num,num*3,num,num*4))
print(' {} x  5 = {}\n {} x  6 = {}\n {} x  7 = {}\n {} x  8 = {}\n {} x  9 = {}\n {} x 10 = {}'.format(num,num*5,num,num*6,num,num*7,num,num*8,num,num*9,num,num*10))
print('='*12)

#ex010

# valor do dólar atualmente

print('_'*7,'CONVERSOR DE MOEDAS','_'*7)
r=float(input('Quantos reais você tem na sua carteira agora mesmo? R$'))
d=r/5.12
print('Você tem {:.2f} dólares US$.'.format(d))

# atividade complementar (euros e won)

real=float(input('Quantos reais você tem na carteira? R$'))
print('Você tem {:.2f} US$ (dólar)\n{:.2f} euros\n{:.2f} won'.format(real/5.12,real/5.48,real*269.32))
