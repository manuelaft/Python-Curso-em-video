# ex025

'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome=str(input('Qual é o seu nome completo? '))
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))

# Nesse caso, o capitalize (primeira letra da str maiúscula) não dá certo porque o que eu quero, o sobrenome, não é o primeiro nome
# Já o title converte as primeiras letras de todas as palavras em maiúsculo