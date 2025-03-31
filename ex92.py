# ex092

'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date as dt
dict={}
dict['Nome']=str(input('Nome: '))
nasc=int(input('Ano de nascimento: '))
sexo=str(input('Sexo [F/M]: ')).strip().upper()[0]
ano=dt.today().year
dict['Idade']=ano-nasc
dict['Carteira de trabalho']=int(input('Carteira de trabalho (0 não tem): '))
if dict['Carteira de trabalho']!=0:
    dict['Ano de contratação']=int(input('Ano de contratação: '))
    dict['Salário']=float(input('Salário: R$'))
    tempo = 35 - (ano-dict['Ano de contratação']) # 35 anos de colaboração para se aposentar
    dict['Aposentadoria']=dict['Idade']+tempo

print('=-'*30)
for keys,value in dict.items():
    print(f'{keys} tem o valor {value}')

print()
print(1990-1991)
