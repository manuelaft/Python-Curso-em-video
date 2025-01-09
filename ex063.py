# ex063

'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.'''

print('='*30)
print('Sequência de Fibonacci')
print('='*30)
num=int(input('Quantos termos você quer mostrar? '))
t1=0
t2=1
print('~'*30)
print(f'{t1} ➞  {t2}',end=' ➞  ')
c=3 # O contador começou no 3 porque já mostrou os termos 1 e 2
while c<=num:
    t3=t1+t2
    print(t3, end=' ➞  ')
    c+=1
    t1=t2 # progressão de termos !! explicação na vídeo aula 
    t2=t3
print(' FIM')
print('~'*30)
