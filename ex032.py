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
if ano%4==0 and ano%100!=0 or ano%400==0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')


'''Considerações finais: eu tive MUITA dificuldade nesse exercício e passei mais de um dia nele 
e surpreendentemente o problema não foi nem o módulo que eu não conhecia porque pesquisei, 
assisti outras vídeos aulas e consegui sacar e tals, nem a estrutura if e else.
O problema mesmo foi o and e or, eu fiquei só no or 
(na verdade nem sabia que existia né eu só pensei isso, coloquei e deu certo) 
mas depois não raciocinei na possibilidade de existir o and, que soma duas condições e não só uma ou outra 
e isso me atrasou demais. Mas mesmo assim consegui fazer do meu jeito mesmo, 
não desisti e presisti, é isso aí. Por mais díficil que as coisas pareçam ser, 
sempre tem uma saída se você for persistente.'''