# ex031

'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

km=int(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} km'.format(km))
if km <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format((km/1)*0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format((km/1)*0.45))

"""Para colocar várias linhas como comentário utlize três aspas"""
