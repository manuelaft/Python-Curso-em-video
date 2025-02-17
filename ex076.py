# ex076

'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
tupla=('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
ímpar=1
for c in range(0,len(tupla),2):
    print(f'{tupla[c]:.<30} R$ ',end='')
    ímpar+=2
    print(f'{tupla[ímpar-2]:>6.2f}')
print('-'*40)
