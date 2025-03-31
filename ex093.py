# ex093

'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador 
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

dict={}
lista=[]
dict['nome']=str(input('Nome do jogador: ')).capitalize()
partidas=int(input(f'Quantas partidas {dict['nome']} jogou? '))
for c in range(0,partidas):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
dict['gols']=lista
dict['total']=sum(lista)
print('=-'*30)
print(dict)
print('=-'*30)
for key,values in dict.items():
    print(f'O campo {key} tem o valor {values}')
print('=-'*30)
print(f'O jogador {dict['nome']} jogou {partidas} partidas.')
for c in range(0,partidas):
    print(f'    => Na partida {c}, fez {lista[c]} gols.')
print(f'Foi um total de {dict['total']} gols\n')
