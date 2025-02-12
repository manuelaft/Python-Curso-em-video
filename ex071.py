# ex071

'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('='*35)
print(f'{'SIMULAÇÃO BANCO':^35}')
print('='*35)

valor=int(input('Qual valor você quer sacar? R$'))

# notas de 50
if valor>=50: # Usar as notas de 50 apenas se o valor for maior ou igual que 50
    print(f'Total de {valor//50} cédulas de R$50.00')

diferença = valor%50 # O que queremos é o restante da divisão por cada cédula (50,20,10,1). Ou seja, o que sobra

# notas de 20
if diferença>=20:
    print(f'Total de {diferença//20} cédulas de R$20.00') # nos dividimos é pela DIFERENÇA, não o valor integral
    
diferença=diferença%20

# notas de 10 
if diferença>=10: # Verifica se há ainda, depoois que retirou as células de 50 e 20, se ainda tem 10 reais para sacar (ou 20 e 1)
    print(f'Total de {diferença//10} cédulas de R$10.00')

diferença=diferença%10

# notas de 1 real
if diferença>=1:
    print(f'Total de {diferença//1} cédulas de R$1.00')

print('='*35)
print('Volte sempre!')