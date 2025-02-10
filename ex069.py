# ex069

'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    
    A) quantas pessoas tem mais de 18 anos.

    B) quantos homens foram cadastrados.

    C) quantas mulheres tem menos de 20 anos.'''

maior18=0
homens=0
mulheres=0
while True:
    print('='*30)
    print(f'{'CADASTRE UMA PESSOA':^25}') #alinhar o texto
    print('='*30)
    i=int(input('Idade: '))
    s=' '
    if i>=18: 
        maior18+=1
    s=str(input('Sexo [M/F]: ')).upper().strip()[0]
    if s=='M':
        homens+=1
    if s=='F' and i>=20:
        mulheres+=1
    print('='*30)
    cont=str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if cont=='N':
        break
print('O total de pessoas com mais de 18 anos: {} \nAo todo temos {} homens cadastrados\nE temos {} mulheres com menos de 20 anos'.format(maior18,homens,mulheres))


# Antes de strings input, é bom inicializar as variáveis e colocar um 'while s not in 'MF': porque muitos users as vezes digitam teclas erradas, é uma medida preventiva