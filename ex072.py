# ex072

'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

extenso=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num=int(input('Digite um número entre 0 e 20: '))
    while num>20:
        num=int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[num]}')
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if resp =='N':
        break
