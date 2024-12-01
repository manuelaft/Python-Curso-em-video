# ex008

''' Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros'''

print('-'*5,'CONVERSOR DE MEDIDAS','-'*5)
m=int(input('Digite um valor em metro: '))
c=m*100
l=m*1000
print('O valor {} em centímetro é {}\nEm milímetro é {}.'.format(m,c,l))

# ver Guanabara:
m=float(input('Digite um valor em metro: '))
print('A medida {} corresponde a:\n{} quilômetros\n{} hectômetros'.format(m,m/1000,m/100))
print('{} decâmetros\n{:.0f} decimetros\n{:.0f} centímetros\n{:.0f} milímetro'.format(m/10,m*10000,m*100,m*1000))
