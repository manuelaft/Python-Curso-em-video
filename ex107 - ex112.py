# ex107 até o ex112

''' ex107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.

ex108: Adapte o código, criando uma função adicional moeda() que consiga mostrar os números como um valor monetário formatado.

ex109: Modifique as funções para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou
não formatado por moeda()

ex110: Adicione uma função chamada resumo(), que mostre na tela as informações em forma de tabela. 

ex111: Crie um pacote que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas para o primeiro pacote e mantenha tudo funcionando.

ex112: Crie uma função no módulo dado chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que seja monetários.'''

from utilidades import moeda,dadoss
while True:
    print()
    preço=dadoss.leia(('Digite o preço: R$'))
    taxa=int(input(f'Deseja calcular o aumento de {moeda.moeda(preço)} em quantos por cento? '))
    desconto=int(input(f'Deseja calcular o desconto de {moeda.moeda(preço)} em quantos por cento? '))
    moeda.resumo(preço,taxa,desconto)
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resposta not in 'SN':
            print('Por favor, digite uma resposta válida!')
    if 'N' in resposta:
        break
print('>> ENCERRADO <<')
