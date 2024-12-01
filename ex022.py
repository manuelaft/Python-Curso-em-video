nome=(input('Digite o seu nome completo: '))
print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
replace=nome.replace(' ','')
print(f'Seu nome possui {len(replace)} letras')
split=nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(split[0], len(split[0])))

#ou (sem variável replace e split)

print(f'Seu nome possui {len(nome.replace(' ',''))} letras')
print('O seu primeiro nome tem {} letras'.format(len(nome.split()[0])))

# versão Guanabara (usando o truque de menos, você pede a lenght da str, mas subtrai todas os ' ' com o count, que conta todos eles por você)

nome=str(input('Digite o seu nome completo: '))
print('Seu nome maiuscúlo é {}'.format(nome.upper()))
print('Seu nome minúsculo é:{}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome)-nome.count(' ')))
print('Já o seu primeiro nome {} tem {} letras'.format(nome.split()[0],len(nome.split()[0])))
