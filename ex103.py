# ex103

'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='',gols=''): # também teria como colocar nome='<desconhecido>'
    if nome=='':
        nome='<desconhecido>'
    if gols.isalpha()==True:
        gols=0
    if gols=='':
        gols=0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

while True:
    print('-'*25)
    nome=str(input('Nome do jogador: ')).capitalize()
    gols=str(input('Quantidade de gols: '))
    ficha(nome,gols)
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Quer continuar? [S/N] ')).upper().split()[0]
        if resposta not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
    if resposta=='N':
        break
print('FICHA ENCERRADA')
