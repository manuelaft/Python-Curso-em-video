#ex011

'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

l=float(input('Digite a largura da parede em metros: '))
a=float(input('Digite a altura da parede em metros: '))
print('Sua parede tem a dimensão de {}x{} e sua área corresponde a {}m2. Correto?\nAgora vamos te ajudar a calcular o quanto de tinta você precisa!\nProcessando... '.format(l,a,l*a))
at=l*a
t=at/2
print('Você vai precisar de {}{}{} litros de tinta'.format('\033[34m',t,'\033[m'))
