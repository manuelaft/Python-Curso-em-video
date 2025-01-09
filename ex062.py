# ex062

'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('=-'*20)
print('GERADOR DE PA')
print('=-'*20)
num=int(input('Primeiro termo: '))
r=int(input('Razão da PA: '))
c=1 # contador dos termos da PA

mais=10 # num inicial de termos a serem mostrados

total=0 # Total de termos

while mais !=0: # enquanto não digitar o 0

    total=total+mais # incrementa o total de termos

    mais+=1 # Itera pelos termos solicitados 

    while c<=total: 

        c+=1 # Incrementa o contador

        num+=r # Calcula o próximo termo da PA

        print(num-r, end=' ➞  ') # exibe o termo atual
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
