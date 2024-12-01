# ver corrigida e simplificada do Guanabara
from random import randint
from time import sleep as s
from colorama import Fore,init
init()
print(Fore.YELLOW +'Suas Opções:',Fore.RESET,'\n[ 0 ]' + Fore.GREEN,'PEDRA',Fore.RESET,'\n[ 1 ]'+ Fore.GREEN, 'PAPEL',Fore.RESET,'\n[ 2 ]'+ Fore.GREEN,'TESOURA',Fore.RESET)
op=int(input('O que você escolheu? ' ))
s(1)
print(Fore.MAGENTA + 'JO...'),s(1)
print('KEN...'),s(1)
print('PO!!!', Fore.RESET),s(1)
print('=-'*20)
lista=('Pedra','Papel','Tesoura') # listas, próxima aula
pc=randint(0,2) # Randint randomiza um número inteiro, nesse caso entre 0 e 2
print('     O computador escolheu',Fore.GREEN + f'{lista[pc]}',Fore.RESET)

#EXPLICAÇÃO lista[pc], sendo pc=random.randint(0,2)

'''Ao fazer isso, você enumera a sua lista e diz ao pc que invés de escrever o número inteiro randomizado
ele deve escrever os NOMES dos itens da lista de acordo com sua enumeração, não um número.
exemplo: print (pc) --> 1 
        print(lista[pc] --> 'Papel' (item de número 1 na lista previamente definida))'''

if op==0:
    print('     O jogador escolheu',Fore.GREEN + 'Pedra',Fore.RESET)
elif op==1:
    print('     O jogador escolheu',Fore.GREEN + 'Papel',Fore.RESET)
elif op==2:
    print('     O jogador escolheu',Fore.GREEN + 'Tesoura',Fore.RESET)
else:
    print('Desculpe, opção inválida.',Fore.RED + 'TENTE NOVAMENTE',Fore.RESET)
print('=-'*20)

if pc==op:
    print(Fore.BLUE + 'EMPATE',Fore.RESET)

elif pc==0:
    if op==1:
        print(Fore.GREEN + 'JOGADOR GANHOU')
        if op==2:
            print(Fore.RED + 'JOGADOR PERDEU')
elif pc==1:
    if op==0:
        print(Fore.RED +'JOGADOR PERDEU')
        if op==2:
            print(Fore.GREEN +'JOGADOR GANHOU')
if pc==2:
    if op==1:
        print(Fore.RED +'JOGADOR PERDEU')
        if op==0:
            print(Fore.GREEN +'JOGADOR GANHOU')

# DICA PARA CONDIÇÕES ANINHADAS

''' Antes de partir direto para o problema, tente estruturar seu pensamento. Nesse exercicio, por exemplo, ficou mais
fácil depois de ter definido que a resposta do computador era o principal e definindo as três primeiras respostas possíveis do pc, 
ai sim viriam as outras condições dentro de cada if, como se fosse um esqueleto. Exemplo:

PRIMEIRO PASSO - 
if pc==0:

elif pc==1:

elif pc==2:

SEGUNDO PASSO - 

Aninhar o restante das condições dentro delas (3 possibilidades para cada resposta do pc), dessa forma ficou mais fácil'''


# você pode alinhar vários if dentro de um if, e vários if dentro de um elif (condições aninhadas)'''