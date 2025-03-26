# ex090

'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
o final, mostre o conteúdo da estrutura na tela.'''

situaçao=dict()
nome=str(input('Nome do aluno: ')).capitalize()
media=float(input(f'Média de {nome}: '))
if media>=7:
    situaçao='aprovado'
if media<7:
    situaçao='recuperação'
if media<6:
    situaçao='reprovado'

print('=-'*30)
print(f' - Nome do aluno é igual a {nome}\n - Média do aluno é igual a {media}\n - Situação do aluno é: {situaçao}')

# ver Guanabara

aluno=dict()
aluno['Nome']=str(input('Nome do aluno: '))
aluno['Média']=float(input(f'Média do {aluno['Nome']}: '))
if aluno['Média']>=7:
    aluno['Situação']='aprovado'
if 5<= aluno['Média']<7:
    aluno['Situação']='recuperação'
else:
    aluno['Situação']='reprovado'

print('=-'*30)
for key,value in aluno.items():
    print(f' - {key} é igual a {value}')
