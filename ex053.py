frase=str(input('Digite uma frase: ')).strip().upper().replace(' ','')
inverso=frase[::-1].replace(' ','').upper().strip()
print('O inverso de {} é {}'.format(frase,inverso))
if inverso==frase:
    print('Temos um palíndromo!')
else:
    print ('A frase digitada não é um palíndromo!')

# MUITO IMPORTANTE!! O fatiamento [::-1] faz a string inverter a ordem! (MACETE)

# Tem como resolver esse exercício usando for e range (ver. Gustavo Guanabara), porém, eu achei + díficil