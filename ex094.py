# ex094

'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário 
e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

dict={}
lista=[]
while True:
    dict['Nome']=str(input('Nome: ')).capitalize()
   
    dict['Sexo']=' '
    while dict['Sexo'] not in 'FM':
        dict['Sexo']=str(input('Sexo: [M/F] ')).upper().split()[0]
        if dict['Sexo']not in'FM':
            print('ERRO! Por favor, digite apenas M ou F.')

    dict['Idade']=int(input('Idade: '))
    lista.append(dict.copy())

    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Quer continuar? [S/N] ')).upper().split()[0]
        if resposta not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
    if resposta=='N':
        break

mulher=[]
pessoas_acima_media=[]
media=0
for item in lista: # item é cada dicionário, logo dict passou a ser item (item['Idade']) !!
    media+=item['Idade'] 
    if item['Sexo']=='F':
        mulher.append(item['Nome'])

''''Se eu usasse dict['Idade'] ia dar errado porque o dicionário está sendo atualizado a cada iteração do loop, 
então mostraria so a idade da pessoa final, diferente da lista que contem os dicionários de TODOS cadastrados (linha 22)'''

print('=-'*30)
print(f'A)  Ao todo temos {len(lista)} pessoas cadastradas')
print(f'B)  A média de idade é de {media/len(lista):.1f} anos.')
print(f'C)  As mulheres cadastradas foram',end=' ')
for i in range(0,len(mulher)):
    print(f'{mulher[i]}',end=' ')
print(f'\nD)  As pessoas com idade acima da média são:')
for item in lista:
    if item['Idade']>(media/len(lista)):
        nada=0
        for key, values in item.items():
            print(f'{key} = {values};',end=' ')
        print()
print()
