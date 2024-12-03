#ex015

'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

print('-'*12,'ALUGUEL DE CARROS','-'*12)
d=int(input('Quantos dias o carro foi alugado? '))
km=float(input('Quantos km o carro rodou durante este período? '))
pd=d*60
pkm=km*0.15
print('O total a pagar é de {}{}{}'.format('\033[32m',pd+pkm,'\033[m'))

# Sempre divida um problema em pequenas tarefas primeiro! Modulize o seu código
