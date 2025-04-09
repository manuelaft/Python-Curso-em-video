# ex101

'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(nasc):
    if 16<=ano-nasc<18 or ano-nasc>=70:
        v='VOTO OPCIONAL'
    elif ano-nasc<16:
        v='VOTO NEGADO'
    elif ano-nasc>=18:
        v='VOTO OBRIGATÓRIO'

    return v

from datetime import datetime # importação global (para o programa todo)
ano=datetime.today().year
print('-'*40)
nasc=int(input('Em que ano você nasceu? '))
voto(nasc)
print(f'Com {ano-nasc} anos: {voto(nasc)}')

# tbm teria como fazer toda essa importação diretamente dentro da def, isso economiza memória (importação local)