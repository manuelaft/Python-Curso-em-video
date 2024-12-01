print('Bem vindo ao nosso site!')
print('='*10,'Cálculo da média!','='*10)
n1=float(input('Digite a sua primeira nota: '))
n2=float(input('Digite a sua segunda nota: '))
m=float(n1+n2)/2
print('Parabéns! Sua média escolar foi {}{:.1f}{}.'.format('\033[35m',m,'\033[m'))

# forma do Guanabara: 

num1=float(input('Primeira nota do aluno: '))
num2=float(input('Segunda nota do aluno: '))
print('A média entre os números {} e {} é {:.1f}'.format(num1,num2,(num1+num2)/2))

# ex008

print('-'*5,'CONVERSOR DE MEDIDAS','-'*5)
m=int(input('Digite um valor em metro: '))
c=m*100
l=m*1000
print('O valor {} em centímetro é {}\nEm milímetro é {}.'.format(m,c,l))

# ver corrigida (Guanabara):
m=float(input('Digite um valor em metro: '))
print('A medida {} corresponde a:\n{} quilômetros\n{} hectômetros'.format(m,m/1000,m/100))
print('{} decâmetros\n{:.0f} decimetros\n{:.0f} centímetros\n{:.0f} milímetro'.format(m/10,m*10000,m*100,m*1000))

