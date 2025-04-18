from utilidades import menu # from utilidades import * (import everything)
from colorama import Fore,init

init(autoreset=True)
def ler_arquivo(opção,arquivo):
    if opção==1:
            menu.cabeçalho('PESSOAS CADASTRADAS')
            arquivo.seek(0)
            print(arquivo.read())
    if opção==2:
            menu.cabeçalho('NOVO CADASTRO')
            while True:
                nome=str(input('Nome: ')) # No py, o input() sempre retorna uma str, por isso try/except ñ da certo aqui
                if nome.isdecimal()==True:
                    print(Fore.RED + 'Encontramos um porblema com o tipo de dado informado')
                else:
                    break
            while True:
                try:
                    idade=int(input('Idade: '))
                except (ValueError, TypeError,KeyboardInterrupt):
                    print(Fore.RED + 'Encontramos um problema com o tipo de dado informado')
                else:
                    break
            print(f'Novo registro de {nome} adicionado')
            tam=40-len(nome)
            arquivo.write(f'{nome}{' '*tam}{idade}\n')
    if opção==3:
            menu.cabeçalho('Saindo do sistema...Até logo!')
            arquivo.close()
