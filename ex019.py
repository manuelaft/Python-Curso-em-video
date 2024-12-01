import random
a1=input('Primeiro aluno: ')
a2=input('Segundo aluno: ')
a3=input('Terceiro aluno: ')
a4=input('Quarto aluno: ')
nomes=[a1,a2,a3,a4]
r=random.choice(nomes)
print(f'O aluno escolhido foi {'\033[34m'}{r}{'\033[m'}')

# ex020

from random import shuffle
a1=str(input('Primeiro aluno: '))
a2=str(input('Segundo aluno: '))
a3=str(input('Terceiro aluno: '))
a4=str(input('Quarto aluno: '))
lista=[a1,a2,a3,a4]
shuffle(lista)
print(f'A ordem de apresentação é\n{lista}')
