# ex051

'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

print('=='*10)
print('10 TERMOS DE UMA PA')
print('=='*10)
termo=int(input('Primeiro termo: '))
r=int(input('Razão: '))
for c in range(10):
    termo+=r
    print(termo-r,end=' ➞  ')
print('ACABOU')

# fórmula matemática do enésimo termo