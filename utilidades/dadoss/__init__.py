def leia(preço):
    from colorama import init,Fore
    init(autoreset=True)
    while True:
        a=str(input(preço).replace(',','.').strip())
        if a.isalpha()==True or a=='':
            print(Fore.RED + ('ERRO! "{}" não é um valor válido.'.format(a)))
        elif a.isdecimal()==True or '.' in a:
            return float(a)
            break
