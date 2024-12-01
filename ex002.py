#ex002

'''Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''

nome=input(f'{'\033[m'}Qual o seu nome? ')
print('Seja muito bem vido à nossa comunidade {}{}{}!'.format('\033[32m',nome,'\033[m'))
