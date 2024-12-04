#ex023

'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

# Tem como fazer utilizando if também

num=int(input('Informe um número: '))
print(f'Analisando o número {num}')
d=num//10
c=num//100
m=num//1000
print('Unidade: {}\nDezena: {}'.format(num%10,d%10))
print('Centena: {}\nMilhar: {}'.format(c%10,m))

''' explicação passo a passo do racicionio:
número 5678 
o símbolo % significa resto da divisão INTEIRA, o número que sobra em baixo antes de você precisar colocar vírgula no resultado !!
5678 % 10 == 8 unidades

Pra pegar só o 7 agora, precisa isolar o 8 transformando em um número depois da vírgula
5678 / 10 == 567.8
5678 // 10 == 567 (o // exclui a vírgula)
567 % 10 == 7 dezenas

5678 (Pra pegar o 6, colocar o 78 depois da vírgula, ou seja, dividir por 100)
5678 // 100 == 56
56 % 10 == 6 centenas

5678 (como é só o 5, dividir por 1000 --> 5.678)
5678 // 1000 == 5'''