# ex035

'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

print('-='*20,'\nAnalisador de Triângulo\n','-='*20)
a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a+b>c and b+c>a and a+c>b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')


# Para melhorar e aperfeiçoar o exercício, no mundo 2 (aula 12) vamos dizer que tipo de triângulo é 
# (escaleno, isosceles, equilatero, retângulo)