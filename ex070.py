# ex070

'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. '''

soma=maior_que_mil=0

menor_preço=float('inf') # inicializar uma variável que começa com um valor MUITO alto (infinito) 
                         # p/ garantir que o para garantir que o primeiro produto cadastrado seja considerado o mais barato no início.

nome_do_produto_mais_barato=' ' # essa variável vai guardar o nome do produto mais barato
while True:
    print('='*40)
    print(f'{'LOJA COMPRE BARATO':^40}')
    print('='*40)
    nome=str(input('Nome do produto: ')).strip()

    preço=float(input('Preço: R$'))
    soma+=preço
        
    if preço<menor_preço: # Se o preço digitado for menor que o da variável menor_preço (o que vai ser),
        
        menor_preço=preço # Atualizamos menor_preço para ser o novo preço.

        nome_do_produto_mais_barato=nome # Atualizamos também nome_do_produto_mais_barato para ser o novo nome
        
    flag=' '
    while flag not in'SN':
        flag=str(input('Quer continuar [S/N]? ')).upper().strip()[0]

    if flag =='N':
        break

print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maior_que_mil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_do_produto_mais_barato} que custa R${menor_preço:.2f}')

# ver Guanabara, também tem como simplificar usando apenas um if

'''menor=contador=0
barato=' '
.
.
.
preço=float(input('Digite aqui o preço: ))

if contador==1: # Ou seja, se for o primeiro valor digitado

    menor=preço # O preço passa a ser o menor
    barato=nome # E o produto barato é o nome do produto que foi digitado

else:

    if preço<menor: # se o segundo e adiante preços forem menores que o primeiro preço digitado
    
    menor=preço # O novo menor preço passa a ser o segundo
    barato=nome # O nome do produto mais barato passa a ser a variável nome'''