#ex007

'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

print('Bem vindo ao nosso site!')
print('='*10,'Cálculo da média!','='*10)
n1=float(input('Digite a sua primeira nota: '))
n2=float(input('Digite a sua segunda nota: '))
m=float(n1+n2)/2
print('Parabéns! Sua média escolar foi {}{:.1f}{}.'.format('\033[35m',m,'\033[m'))

