v=input(f'Escreva algo: {'\033[31m'}')
print('{}O tipo primitivo desse valor é {}'.format('\033[m',type(v)))
print('Só tem espaços?',v.isspace())
print('É um número?',v.isnumeric())
print('É alfabético?',v.isalpha())
print('É alfanúmerico?',v.isalnum())
print('Está em minúsulo?',v.islower())
print('Está em maiúsculo?',v.isupper())
print('Está capitalizada?',v.istitle())

# v é um OBJETO

# utilizando o format:

v=input(f'Whats on your mind?{'\033[36m'} ')
print('{}O tipo primitivo desse valor é {}'.format('\033[m',type(v)))
print('Só tem espaços? {}'.format(v.isspace()))
print('É um número? {}'.format(v.isnumeric()))
print('É alfabético? {}'.format(v.isalpha()))
print('É alfanúmerico? {}'.format(v.isalnum()))
print('Está em minúsulo? {}'.format(v.islower()))
print('Está em maiúsculo? {}'.format(v.isupper()))
print('Está capitalizada? {}'.format(v.istitle()))
