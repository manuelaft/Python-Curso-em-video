# ex077

'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras=('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
print('-'*40)
for c in palavras:
    print(f'\nNa palavra {c} temos',end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}',end=' ')
print('\n')
print('-'*40)

# explicação: Apesar das palavras (strings) estarem numa tupla, cada uma delas continua sendo uma lista !
# Usamos o for letra in c (c é cada palavra da tupla), para assim o for percorrer cada letra da lista, 
# ou seja cada letra de cada palavra. E dentro do for colocamos uma verificação se é vogal ou não, e se fosse, printar.
