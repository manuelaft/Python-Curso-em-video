# ex066

'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

c=s=0
while True:
    num=int(input('Digite um valor (999 para parar): '))
    if num==999:
        break
    s+=num
    c+=1 # embaixo do break para o flag não ser contado
    
print(f'A soma dos {c} valores foi {s}!')
