# ex042

'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes'''

a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a+b>c and b+c>a and a+c>b:
    cond=bool(True)
else:
    cond=bool(False)

if cond==True and a==b==c:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif cond==True and a!=b!=c and b!=c!=a and c!=a!=b:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
elif cond==True and a==b and c!=a or b==c and a!=b or a==c and b!=c:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
elif cond==False:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
    