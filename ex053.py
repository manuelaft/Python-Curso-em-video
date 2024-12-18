# ex053

'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase=str(input('Digite uma frase: ')).strip().upper().replace(' ','')
inverso=frase[::-1].replace(' ','').upper().strip()
print('O inverso de {} é {}'.format(frase,inverso))
if inverso==frase:
    print('Temos um palíndromo!')
else:
    print ('A frase digitada não é um palíndromo!')

# MACETE!! O fatiamento [::-1] faz a string inverter a ordem!

# Tem como usaR for e range (ver. Gustavo Guanabara) + díficil