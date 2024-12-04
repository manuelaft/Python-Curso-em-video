# ex027

'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome=str(input('Qual é o seu nome completo? ')).strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[-1]))

# Para acessar algum elemento da lista em específico se usa as chaves, mas quando você quer o último, usa-se os números negativos
# Por exemplo, [-1] --> último
# [-2] --> penúltimo, e assim por diante