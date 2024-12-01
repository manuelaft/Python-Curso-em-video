import math
numero=float(input('Digite um ângulo: '))
r=math.radians(numero)
print(f'O seno do ângulo {numero} é {math.sin(r):.2f}\nO cosseno é {math.cos(r):.2f}')
print(f'E a tangente é {math.tan(r):.2f}')

#Simplificando o máximo que eu consigo o código

from math import sin, cos, tan, radians
num=float(input('Escreva um valor: '))
print('O seno do ângulo {} é {:.2f}'.format(num,sin(radians(num))))
print('O cosseno é {:.2f}'.format(cos(radians(num))))
print('E a tangente é {:.2f}'.format(tan(radians(num))))

#O radians pode ser integrado dentro da própria função sin/cos/tan
# Usando o round para definir quantas casas após a vírgula

Valor=5.876549020
print(round(Valor,3))