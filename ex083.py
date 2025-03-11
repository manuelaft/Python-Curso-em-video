# ex083

'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

x=str(input('Digite a expressão: '))
p1=x.count('(')
p2=x.count(')')
if p1!=p2:
    print('Sua expressão está inválida!')
else:
    print('Sua expressão está válida!')

# não considera )a + b( como inválida! 

# --> método da pilhas