# ex086

'''Crie um programa que declare uma matriz de dimensão 3 x 3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.'''

matriz=[[0,0,0],[0,0,0],[0,0,0]] # cada uma das listas representa uma linha da matriz

for linha in range(0,3):
    for coluna in range(0,3):
        num=int(input(f'Digite um valor para a posição [{linha},{coluna}]: '))
        matriz[coluna][linha]=num

for contador in range(0,3):
    print(f'[ {matriz[0][contador]:>3} ] [ {matriz[1][contador]:>3} ] [ {matriz[2][contador]:>3} ]')

# inicio uso de matrizes
