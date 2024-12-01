n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
m=(n1+n2)/2
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(n1,n2,m))
if m < 5.0:
    print('O aluno está REPROVADO!')
elif 5.0 <= m < 6.9:
    print('O aluno está em RECUPERAÇÃO.')
elif m >= 7.0:
    print('O aluno está APROVADO, parabéns!')

