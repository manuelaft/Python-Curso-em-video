print('=-'*20)
print('Gerador de PA')
print('=-'*20)
num=int(input('Primeiro termo: '))
r=int(input('Razão da PA: '))
c=1 # variavél contadora
while c<=10:
    c+=1 # quantidade de vezes !
    num+=r
    print(f'{num-r}',end=' ➞  ')
print(' FIM')
