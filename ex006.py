#ex006

'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

n=int(input('Digite um valor: '))
m=n*2
t=n*3
r=float(pow(n,1/2))
print('O dobro do número {} é {}, o triplo é {}\nEnquanto a raiz quadrada desse número é {:.2f}'.format(n,m,t,r))

#{} == mascara 

# ou também:
n1=int(input('Digite um valor: '))
print('O dobro do múmero {} é {}, o triplo é {}\ne a raiz quadrada de {} é {}'.format(n1,n1*2,n1*3,n,pow(n,(1/2))))
