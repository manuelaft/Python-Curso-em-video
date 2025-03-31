# ex091

'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint as ri
maior=0
dicionario={'Jogador 1':ri(1,6),'Jogador 2':ri(1,6),'Jogador 3':ri(1,6),'Jogador 4':ri(1,6)}
print('Valores sorteados: ')
for c in range(0,4):
    print(f'Jogador {c+1} tirou {dicionario.get(f'Jogador {c+1}')} no dado')
print('=-'*15)
print(f'{'= RANKING DOS JOGADORES =':^30}')

for posicao, i in enumerate(sorted(dicionario, key=dicionario.get, reverse=True)):
    print(f'{posicao+1}º lugar: {i} com {dicionario[i]}')

# O enumerate adiciona um contador automático no loop (sem precisar fazer dois for, que como nesse caso, não dá certo)