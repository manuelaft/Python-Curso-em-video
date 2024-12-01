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
    