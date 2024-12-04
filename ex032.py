# ex032

'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

import datetime as dt
ano=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano=dt.datetime.today().year

if ano%100 != 0 or ano%400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

# != diferente de

# versão corrigida do Guanabara:

from datetime import datetime
ano=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano=datetime.today().year
if ano%4==0 and ano%100!=0 or ano%400==0: #and !!
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')

