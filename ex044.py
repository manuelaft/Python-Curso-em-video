# ex044

'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros'''

print('='*10,'\033[32m LOJINHA ARTESANAL \033[m','='*10)
price=float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro
[ 2 ] cartão de débito
[ 3 ] cartão de crédito 2x sem juros
[ 4 ] cartão de crédito 3x ou mais com juros''')
op=int(input('Qual é a opção desejada? '))
if op == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price,(price-(10*price)/100)))
elif op==2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price,price-(5*price)/100))
elif op==3:
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} SEM JUROS.'.format(price,price/2))
elif op==4:
    parc=int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(parc,((20*price)/100 + price)/parc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(price,price+(20*price)/100))
else:
    print('\033[31mOpção inválida de pagamento. TENTE NOVAMENTE \033[m')

# Observação: Tem como fazer criando uma variável dentro de cada elif

