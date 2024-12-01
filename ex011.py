l=float(input('Digite a largura da parede em metros: '))
a=float(input('Digite a altura da parede em metros: '))
print('Sua parede tem a dimensão de {}x{} e sua área corresponde a {}m2. Correto?\nAgora vamos te ajudar a calcular o quanto de tinta você precisa!\nProcessando... '.format(l,a,l*a))
at=l*a
t=at/2
print('Você vai precisar de {}{}{} litros de tinta'.format('\033[34m',t,'\033[m'))

# ex012

print(' ')
print('Uma loja aplicou um desconto de 5% no valor de seu produto que originalmente custava ')
o=float(input('Digite o preço orginal do produto: R$'))
d=o*5/100
print('E agora, depois do desconto passou a custar {:.2f} reais'.format(o-d))
