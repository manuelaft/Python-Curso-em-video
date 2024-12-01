n=int(input('Digite um valor qualquer: '))
s=n+1
a=n-1
print('O número antecessor do número {} é {}{}{}, e o seu sucessor é {}{}{}'.format(n,'\033[33m',a,'\033[m','\033[33m',s,'\033[m'))

# utilizando uma variável (forma do Guanabara):

n=int(input('Digite um valor qualquer: '))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor {}'.format(n,(n-1),(n+1)))

# ex006

n=int(input('Digite um valor: '))
m=n*2
t=n*3
r=float(pow(n,1/2))
print('O dobro do número {} é {}, o triplo é {}\nEnquanto a raiz quadrada desse número é {:.2f}'.format(n,m,t,r))

#{} == mascara 

# ou (forma do Guanabara):

n1=int(input('Digite um valor: '))
print('O dobro do múmero {} é {}, o triplo é {}\ne a raiz quadrada de {} é {}'.format(n1,n1*2,n1*3,n,pow(n,(1/2))))
