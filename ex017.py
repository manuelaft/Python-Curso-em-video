# h2 = o2 +a2
import math
o=float(input('Digite o comprimento do cateto oposto em metros: '))
a=float(input('Digite o comprimento do cateto adjacente em metros: '))
print(f'A hipotenusa de um triângulo retângulo cujo medidas são {o} e {a} é {math.hypot(o,a):.2f}')

# do jeito matemático, sem importação

co=float(input('Qual o valor do cateto oposto? '))
ca=float(input('Qual o valor do cateto adjacente? '))
hi=(co**2+ca**2)**(1/2)
print('A hipotenusa é {}{:.2f}{}'.format('\033[35m',hi,'\033[m'))
