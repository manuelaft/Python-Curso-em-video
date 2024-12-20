# ex056

'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

idades=[]
nome_homem=''
idade_homem=0
idade_mulher=[]
for c in range(1,5):
    print('―――――― {}ª PESSOA ――――――'.format(c))
    n=str(input('Nome: ')).strip()
    i=int(input('Idade: '))
    s=str(input('Sexo [M/F]: ')).strip().upper()
    idades+=[i]
    if s=='M' and i>idade_homem:
        idade_homem=i
        nome_homem=n

    if s=='F':
        if i<20:
            idade_mulher+=[i]

soma=int(sum(idades))
print('A média de idade do grupo é {:.1f} anos'.format(soma/4))
print(f'O homem mais velho tem {idade_homem} e se chama {nome_homem}.')
print('Ao todo são {} mulheres com menos de 20 anos'.format(len(idade_mulher)))

# versão corrigida do Guanabara:

if c==1 and s=='M': 
    idade_homem=i
    nome_homem=n
if s=='M' and i>idade_homem: 
    i=idade_homem 
    nome_homem=n 

# Correção último item, quantas mulheres menores de 20 anos

mulheres_menoresidades=0
if s=='F' and i<20:
    mulheres_menoresidades+=1 