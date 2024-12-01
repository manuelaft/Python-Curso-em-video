soma=0
qt=0 # isso se chama contador, semelhante ao conceito de acumulador, mas serve para contar quantos itens dentro do for
for c in range(1,7):
    n=int(input('Me fale um número: '))
    if n%2==0:
        qt = qt +1 # também vai ser explicado na aula 14
        soma+=n

print('Você informou {} números pares e a soma entre eles é igual {}'.format(qt,soma))
