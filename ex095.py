# ex095

'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

dict={}
lista=[]
while True:
    print('=-'*30)
    quant_gols=[]
    dict['nome']=str(input('Nome do jogador: ')).capitalize()
    dict['partidas']=int(input(f'Quantas partidas {dict['nome']} jogou? '))
    for c in range(0,dict['partidas']):
        gols=int(input(f'Quantos gols na partida {c}? ')) # dict['gols'] -> a cada vez que o loop itera, atualiza
        quant_gols.append(gols)
        dict['gols']= quant_gols[:] # armazenando TODOS os valores de 'gols' em uma lista dentro de um dicionário
    dict['total']=sum(quant_gols)
    lista.append(dict.copy())
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if resposta=='N':
        break
print('=-'*30)
print(f'{'cod nome':<20}{'gols'}{'total':>20}')
print('-'*60)
for indice,valores in enumerate(lista):
    print(f'{indice} {str(valores['nome']):<17}',end=' ')
    print(f'{str(valores["gols"]):<17}',end=' ') # tranformar para str antes porque o py não aceita formatação (:>15) em listas, apenas num e str
    print(f'{str(valores['total']):>6}',end=' ')
    print()
while True:
    print('-'*60)
    dados=int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados==999:
        break
    elif dados>len(lista):
        print(f'ERRO! Não existe jogador com código {dados}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[dados]['nome']}:')
        for c in range(0,lista[dados]['partidas']):
            print(f'No jogo {c} fez {lista[dados]['gols'][c]} gols.')
print('<< ACABOU >>\n')
