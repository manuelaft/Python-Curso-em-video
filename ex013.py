s=float(input('Digite o seu atual salário: '))
v=int(input('Qual a porcentagem do seu aumento salarial? '))
a=s*v/100
t=s+a
print('Parabéns! Seu novo salário vai ser {}{:.2f}{}'.format('\033[32m',t,'\033[m'))

# teste

v=float(input('Qual o preço do produto? R$'))
vista=v*10/100
d=v-vista
print('Pagando à vista, você recebe 10% de desconto! Ficando {}'.format(d))
parcelado=v*5/100
p=parcelado+v
print('Pagando à prazo, temos uma taxa adicional de 5%. Ficando {}'.format(p))
div=p/2
print('Com parcelas de até 2x sem juros!\n2x de {}'.format(div))

# ex014

c=float(input('Me informe a temperatura em Celsius: '))
f=(c*1.8)+32
print('A temperatura de {}C corresponde à {} Farenheit'.format(c,f))