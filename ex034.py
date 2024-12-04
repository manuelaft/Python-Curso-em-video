# ex034

'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

s=int(input('Qual é o salário do funcionário? R$'))
if s<=1250:
    a=(15/100)*s
else:
    a=(10/100)*s
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s, s+a))
