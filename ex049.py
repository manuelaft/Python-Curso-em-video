# ex049

'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num=int(input('Digite um número para saber sua tabuada: '))
print('=='*10)
for c in range(0,11):
    print(f'{num} x {c} = {num*c}')
print('=='*10)