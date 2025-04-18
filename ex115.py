# ex115

'''Crie um menu em Python, que tenha acesso a arquivos e usando modularização.'''

from utilidades import menu,dadoss,arquivos
from colorama import Fore, init

init(autoreset=True)
opção=0
arquivo=open('arquivo.txt','a+') # 'a' de modo append, '+' p/ poder ler e escrever no arquivo! 
while opção!=3:
    menu.cabeçalho('MENU PRINCIPAL')
    menu.menu()
    opção=dadoss.Opção(Fore.YELLOW + 'Sua opção: ')
    arquivos.ler_arquivo(opção,arquivo)
