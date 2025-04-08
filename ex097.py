# ex097

'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(texto):
    l=len(texto)+4
    print('~'*l)
    print(f'  {texto}')
    print('~'*l)

while True:
    txt=str(input('Escreva algo: '))
    escreva(txt)
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if resp=='N':
        break
print('Finalizando...')
