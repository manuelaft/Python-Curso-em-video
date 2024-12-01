frase=str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.lower().find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.lower().rfind('a')+1))

#linha 3: o +1 é para aparecer a posição como nos somos acostumados (posição 1), já que o pc sempre começa com 0
#linha 4: rfind significa procurar começando pela direita da str, ou seja, final


# ex027

nome=str(input('Qual é o seu nome completo? ')).strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[-1]))

# Para acessar algum elemento da lista em específico se usa as chaves, mas quando você quer o último, os números negativos fazem isso
# Por exemplo, [-1] --> último
# [-2] --> penúltimo, e assim por diante