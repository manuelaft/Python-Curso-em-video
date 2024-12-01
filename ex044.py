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

# Observação ! Existe outras formas de resolver o mesmo exercício. Na ver do Guanabara, ele criou uma variável dentro de cada elif
# invés de colocar tudo no format e economizar nas variáveis. Exemplo: desconto = price*10/100 - price

