# ex039

'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import datetime as dt
ano=int(input('Ano de nascimento: '))
sex=str(input('Você é do sexo biológico masculino ou feminino? '))
if sex=='masculino':
    sex=1
else:
    sex=2
atual=dt.today().year
idade=(atual-ano)
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,atual))
if sex==2:
    print('O alistamento no serviço militar brasileiro não é obrigatório para você!')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-idade))
    print('Seu alistamento será em {}.'.format(atual+(18-idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(idade-18))
    print('Seu alistamento foi em {}'.format(atual-(idade-18)))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
