from emoji import emojize
from time import sleep as s
for c in range(10,0-1,-1):
    s(1)
    print(c)
print(emojize('BOOM! :fireworks::sparkle:'))

# ex047

for c in range(2,50+1,2):
    print(f'{c}',end=' ') 
print('FIM')

# Se quisermos imprimir texto na mesma linha em Python, podemos usar end e o defininir logo depois com uma string vazia ou qualquer outro caractere.
