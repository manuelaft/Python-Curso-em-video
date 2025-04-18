from colorama import init,Fore
init(autoreset=True)

def leia(preço):
    while True:
        a=str(input(preço).replace(',','.').strip())
        if a.isalpha()==True or a=='':
            print(Fore.RED + ('ERRO! "{}" não é um valor válido.'.format(a)))
        elif a.isdecimal()==True or '.' in a:
            return float(a)
            break

def Opção(opção): # Tratamento de erros de opções do usuário no menu
    while True:
        try:
            a=int(input(opção))
            if int(a)>=4:
                print(Fore.RED + 'Por favor, digite um valor entre 1 e 3 apenas')
            else: 
                return a
        except (ValueError,TypeError,KeyboardInterrupt):
            print(Fore.RED + 'Ops! Por favor informe um número inteiro válido')
        else:
            return a
            break
