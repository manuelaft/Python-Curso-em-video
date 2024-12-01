v=float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite de 80 km/h permitido')
    print('Você deve pagar uma multa de R${:.2f}'.format((v-80)*7))
print('Tenha um bom dia ! Dirija com segurança !')

# ex030

num=int(input('Me diga um número qualquer: '))
if num%2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))

# ex031

km=int(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} km'.format(km))
if km <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format((km/1)*0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format((km/1)*0.45))

"""Para colocar várias linhas como comentário utlize três aspas"""

