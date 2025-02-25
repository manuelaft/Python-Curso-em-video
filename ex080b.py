# ex080 - versão b

lista=list()
for c in range(0,5):
    n=int(input(f'Digite um valor para a posição {c}: '))
    if c==0 or n>lista[-1]: # n maior que o elemento *anterior* da lista
        lista.append(n)
        print('Valor adicionado ao final da lista')
    else:
        posiçao=0
        while posiçao<len(lista):
            if n <=lista[posiçao]:
                lista.insert(posiçao,n)
                print(f'Valor adicionado na posição {posiçao} da lista')
                break
            posiçao+=1
print('=-'*30)
print(f'Os valores digitados em ordem foram {lista}')
