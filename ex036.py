casa=float(input('Valor da casa: R$'))
s=float(input('Salário do comprador: R$'))
anos=int(input('Quantos anos de financiamento? '))
print('Para pagar uma casa de R${:.2f} em {} anos a prestação mensal será de R${:.2f}'.format(casa,anos,casa/(anos*12)))
if casa/(anos*12)>=s*30/100:
    print( 'Empréstimo foi NEGADO!')
else:
    print('Empréstismo pode ser CONCEDIDO!')
