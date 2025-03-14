# ex087

'''Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
    B) A soma dos valores da terceira coluna.                                                                                                                
        C) O maior valor da segunda linha.'''

matriz=[[0,0,0],[0,0,0],[0,0,0]]
pares=[]
coluna3=list()
linha2=list()
for linha in range(0,3):
    for coluna in range(0,3):
        num=int(input(f'Digite um valor para a posição [{linha},{coluna}]: '))
        matriz[coluna][linha]=num
        if num%2==0:
            pares.append(num)
for c in range(0,3):
    coluna3.append(matriz[2][c])
    linha2.append(matriz[c][1])
print('=-'*30)
for contador in range(0,3):
    print(f'[ {matriz[0][contador]:>2} ] [ {matriz[1][contador]:>2} ] [ {matriz[2][contador]:>2} ]')
print('=-'*30)
print(f'A soma dos valores pares é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {sum(coluna3)}')
print(f'O maior valor da segunda linha é {max(linha2)}')
