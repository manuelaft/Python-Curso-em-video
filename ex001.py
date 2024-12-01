#Teste 1

# Aula 11 - desafio do chefão (colocar cores em todos os exercícios !!)

cores={'limpa':'\033[m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'amarelo':'\033[33m',
       'azul':'\033[34m',
       'roxo':'\033[35m',
       'verdeagua':'\033[36m',
       'cinza':'\033[37m'}

name=input('\033[mDigite o seu nome: ')
idade=input('Digite a sua idade: ')
peso=input('Digite o seu peso: ')
print(f'{cores['verde']}{name}{cores['limpa']}, {cores['verdeagua']}{idade}{cores['limpa']}, {cores['roxo']}{peso}{cores['limpa']}')

# desafio de número 1
nome=input('Me fale o seu melhor apelido: ')
print(f'Olá {cores['vermelho']}{nome}{cores['limpa']}, é um prazer te conhecer!')

# desafio de número 2
dia=input('Que dia você nasceu? ')
mês=input('Qual mês você nasceu? ')
ano=input('Qual ano você nasceu? ')
print(f'Você nasceu no dia {cores['amarelo']}{dia}{cores['limpa']} de {cores['verde']}{mês}{cores['limpa']} de {cores['azul']}{ano}{cores['limpa']}.Correto?')

# desafio de número 3
nu1=input('Digite um número: ')
nu2=input('Digite um segundo número: ')
print(f'A soma entre eles é {cores['verdeagua']}{nu1+nu2}{cores['limpa']}')
