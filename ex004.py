#ex004

'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

v=input(f'Escreva algo: {'\033[31m'}')
print('{}O tipo primitivo desse valor é {}'.format('\033[m',type(v)))
print('Só tem espaços?',v.isspace())
print('É um número?',v.isnumeric())
print('É alfabético?',v.isalpha())
print('É alfanúmerico?',v.isalnum())
print('Está em minúsulo?',v.islower())
print('Está em maiúsculo?',v.isupper())
print('Está capitalizada?',v.istitle())

# v é um OBJETO
