# ex048

'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

soma=0 # acumuladores (aula 14)
quantidade=0
for num in range (0,500+1,3):
    if num %2!=0: # ou seja, se ele for ímpar

        soma+=num # += somatório de todos os elementos num, mas para isso precisa de um acumulador, geralmente de valor zero

        lista=[num] # o len só pega em string e em listas, por isso, para usar ele, precisei criar uma lista com os números num
        quantidade+=len(lista) 
    
print('Existem {} números múltiplos de 3, que estão entre 1 e 500.'.format(quantidade-1)) # menos 1 por causa do zero
print('A soma de todos os números múltiplos de 3, que estão entre 1 e 500, é igual a {}'.format(soma))
