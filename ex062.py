# ex062

'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('=-'*20)
print('Gerador de PA')
print('=-'*20)
num=int(input('Primeiro termo: '))
r=int(input('Razão da PA: '))
c=0
mais=int(10)
while mais!=0:
    while c<10:
        c+=1
        num+=r
        print(num-r, end=' ➞  ')
    print('PAUSA')
    mais=input('Quantos termos a mais você quer mostrar? ')
    while mais<10:
        mais+=r
        print(mais)

