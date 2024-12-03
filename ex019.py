#ex019

'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random
a1=input('Primeiro aluno: ')
a2=input('Segundo aluno: ')
a3=input('Terceiro aluno: ')
a4=input('Quarto aluno: ')
nomes=[a1,a2,a3,a4]
r=random.choice(nomes)
print(f'O aluno escolhido foi {'\033[34m'}{r}{'\033[m'}')

