# ex062

'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('=-'*20)
print('GERADOR DE PA')
print('=-'*20)
num=int(input('Primeiro termo: '))
r=int(input('Razão da PA: '))
c=1
mais=10
total=0
while mais !=0:
    total=total+mais
    mais+=1
    while c<=total:
        c+=1
        num+=r
        print(num-r, end=' ➞  ')
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))


