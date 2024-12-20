# ex057

'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

s=str(input('Informe o seu sexo [M/F]: ')).upper().strip() [0] # Fatiamento p/ aparecer apenas a primeira letra caso a pessoa digite 'masculino'
if s in 'MFmf':
    print(f'Sexo {s} registrado com sucesso')
    s=True
else:
    s=False
while s==False:
    sexo=str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
    if sexo in 'MmFf':
        print(f'Sexo {sexo} registrado com sucesso')
        s=True

# início da validação de dados

# Correção do Guanabara

sex=str(input('Informe o seu sexo: ')).upper().strip() [0]
while sex not in 'MFmf':  # MUITA ATENÇÃO NO NOT IN !!
    sex=str(input('Dados inválidos. Por favor digite novamente: ')).upper().strip() [0]
print(f'Sexo {sex} registrado com sucesso')
