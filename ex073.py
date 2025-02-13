# ex073

'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da sua preferência.'''


times=('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthians','Bahia','Cruzeiro','Vasco da Gama',
'EC Vitória','Atlético-MG','Fluminense','Grêmio','Juventude','Bragantino','Athletico-PR','Criciúma','Atlético-GO','Cuiabá')
print('=-'*90)
print('LISTA DE TIMES DO BRASILEIRÃO:\n',end='')
for contador in range(0,20):
       print(f'{times[contador]}')
print('=-'*90)
print(f'Os 5 primeiros colocados são: {times[0]}, {times[1]}, {times[2]}, {times[3]} e {times[4]}')
print('=-'*90)
print(f'Os 4 últimos colocados são {times[-4]}, {times[-3]}, {times[-2]} e {times[-1]}')
print('=-'*90)
print('Times organizados em ordem alfabética:\n')
tupla=sorted(times)
for contador in range(0,20):
       print(f'{tupla[contador]}')
print('=-'*90)
while True:
       resp=' '
       while resp not in times:
              resp=str(input('Você quer saber a posição de qual time? ')).strip().capitalize()
       index=times.index(resp)
       print(f'O time {times[index]} está na {index+1}ª posição')
       print(' ')
       resp2=' '
       while resp2 not in 'SN':
              resp2=str(input('Deseja saber de mais algum outro [S/N]? ')).strip().upper()[0]
       if resp2=='N':
              break
print('OK! Muito obrigada e volte sempre.')
