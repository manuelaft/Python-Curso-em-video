#ex001

'''Crie um programa que escreva "Olá,Mundo!" na tela'''

cores={'limpa':'\033[m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'amarelo':'\033[33m',
       'azul':'\033[34m',
       'roxo':'\033[35m',
       'verdeagua':'\033[36m',
       'cinza':'\033[37m'}

print(f'{cores['vermelho']}Olá,Mundo!{cores['limpa']}')