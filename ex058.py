# ex058

'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from time import sleep
import random
n=random.randint(0,10)
tentativas=0
print('=-'*20,'\n',' '*4,'JOGO: ADIVINHE O NÚMERO 2.0\n','=-'*20)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10\nSerá que você consegue adivinhar qual foi?')
usuario=int(input('Qual é o seu palpite? '));sleep(3)
while usuario!=n:
    if n>usuario:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    usuario=int(input('Qual é o seu palpite? '));sleep(3)
    tentativas+=1
sleep(3)
print(f'Acertou com {tentativas+1} tentativas. Parabéns!')

# tem como resolver utilizando True e False também, semelhantemente ao último exercício.
