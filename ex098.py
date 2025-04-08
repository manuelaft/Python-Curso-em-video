# ex098

'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:    

a) de 1 até 10, de 1 em 1                                                                                                                                              
    b) de 10 até 0, de 2 em 2                                                                                                                                            
        c) uma contagem personalizada'''

from time import sleep
print()
def contador(a,b,c):
    
    if a>b:
        c=-abs(c) # abs() -> modulização  ;  -abs() -> transforma em negativo

    print('=-'*20)
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')

    if a>b:
        b=b-1
    elif b>a:
        b=b+1

    for c in range(a,b,c):
        print(f'{c}',end=' ',flush=True) # sem o flush (atualização) o sleep não é para cada valor, apenas no começo
        sleep(0.5)
    print('FIM')
    print('=-'*20)

contador(1,10,1)
contador(10,0,2)

inicio=int(input('Agora é a sua vez de personalizar a contagem!\nInício: '))
fim=int(input('Fim:    '))
passo=int(input('Passo:  '))
if passo==0:
    passo=1

contador(inicio,fim,passo)
print()