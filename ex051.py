print('=='*10)
print('10 TERMOS DE UMA PA')
print('=='*10)
termo=int(input('Primeiro termo: '))
r=int(input('Razão: '))
for c in range(10):
    termo+=r
    print(termo-r,end=' ➞  ')
print('ACABOU')

# tem como resolver pela fórmula matemática do enésimo termo também