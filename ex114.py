# ex114

'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib.request
from colorama import init,Fore

init(autoreset=True)
print()
try:
    urllib.request.urlopen('https://www.pudim.com.br') # site = 
    print(Fore.GREEN + 'O site pudim está disponivel no momento')
except urllib.error.URLError: 
    print(Fore.YELLOW + 'O site pudim não está disponivel no momento')
print()

# print(site.read()) --> É possível ler TODO o conteúdo HTML de qualquer site !