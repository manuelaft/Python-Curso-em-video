print('~'*10,'\033[35m CÁLCULO DO ÍNDICE DE MASSA CORPORAL\033[m','~'*10)
p=float(input('Qual é o seu peso? (kg) '))
m=float(input('Qual é a sua altura? (m) '))
imc=p/(m**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 25 > imc >= 18.5:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 40 > imc >= 30:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')