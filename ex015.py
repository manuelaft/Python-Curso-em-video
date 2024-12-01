print('-'*12,'ALUGUEL DE CARROS','-'*12)
d=int(input('Quantos dias o carro foi alugado? '))
km=float(input('Quantos km o carro rodou durante este período? '))
pd=d*60
pkm=km*0.15
print('O total a pagar é de {}{}{}'.format('\033[32m',pd+pkm,'\033[m'))

# Sempre divida um problema em pequenas tarefas primeiro! Modulize o seu código

# ex016

from math import trunc
num=float(input('Digite um valor: '))
print('O valor digitado, {} e a sua porção inteira é {}'.format(num,trunc(num)))

# Sem utilizar de nenhuma biblioteca também tem como fazer esse exercício:

n=float(input('Digite um número: '))
print('O número digitado foi {} e sua parte inteira é {}'.format(n,int(n)))
