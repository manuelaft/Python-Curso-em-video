s=int(input('Qual é o salário do funcionário? R$'))
if s<=1250:
    a=(15/100)*s
else:
    a=(10/100)*s
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s, s+a))

# ex035

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