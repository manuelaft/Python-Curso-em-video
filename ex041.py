from datetime import datetime as dt
atual=dt.today().year
ano=int(input('Ano de nascimento: '))
print('O atleta tem {} anos.'.format(atual-ano))
if atual-ano <= 9:
    print('Classificação: MIRIM')
elif 9 < atual-ano <= 14:
    print('Classificação: INFANTIL')
elif 14 < atual - ano <= 19:
    print('Classificação: JÚNIOR')
elif 19 < atual - ano <= 25:
    print('Classificação: SÊNIOR')
elif atual-ano > 25:
    print('Classificação: MASTER')
