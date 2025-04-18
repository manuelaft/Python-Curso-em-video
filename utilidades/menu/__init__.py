from colorama import Style,Fore,init
init(autoreset=True)

def cabeçalho(txt):
    print(Style.RESET_ALL)
    print('-'*42)
    print(txt.center(42))
    print('-'*42)

def menu():
    print(Fore.YELLOW + '1',end=' - ')
    print(Fore.BLUE + 'Ver pessoas cadastradas')
    print(Fore.YELLOW + '2',end=' - ')
    print(Fore.BLUE + 'Cadastrar nova pessoa')
    print(Fore.YELLOW + '3',end=' - ')
    print(Fore.BLUE + 'Sair do sistema')

