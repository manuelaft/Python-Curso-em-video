# ex106

'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra "FIM", o programa se encerrará. Importante: use cores.'''

from colorama import init, Fore, Back, Style
init()
def cabeçalho(texto):
    tam=len(texto)+3
    print(Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.MAGENTA)
    print('~'*tam)
    print(texto)
    print('~'*tam + Style.RESET_ALL)

def manual(txt):
    tam=len(txt)+3
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT)
    print('~'*tam)
    print(txt)
    print('~'*tam + Style.RESET_ALL)

def fim(msg):
    tam=len(msg)+3
    print(Back.RED + Fore.WHITE + Style.NORMAL)
    print('~'*tam)
    print(msg)
    print('~'*tam + Style.RESET_ALL)

while True:
    cabeçalho(f'{'  SISTEMA DE AJUDA PY':^3}')
    resposta=str(input('Função ou Biblioteca > '))
    if resposta=='fim':
        fim(f'{'    ATÉ LOGO!'}')
        break
    manual(f'{' Acessando o manual da função "{}"...'}'.format(resposta))
    print(Fore.BLACK + Back.WHITE + Style.NORMAL)
    print(help(resposta))
    print(Style.RESET_ALL)
