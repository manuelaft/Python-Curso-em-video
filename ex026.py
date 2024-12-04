# ex026

'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez'''

frase=str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.lower().find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.lower().rfind('a')+1))

#linha 3: o +1 é para aparecer a posição como nos somos acostumados (posição 1), já que sempre começa com 0 a contagem
#linha 4: rfind significa procurar começando pela direita da str, ou seja, final
