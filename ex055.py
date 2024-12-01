pesos=[]
for c in range (1,6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    pesos+=[peso]
print('O maior peso lido foi de {} Kg'.format((max(pesos))))
print('O menor peso lido foi de {} Kg'.format(min(pesos)))

''' O min e o max funciona com listas, strings, etc. Por isso é preciso colocar os valores float dentro de uma lista
Se eu não criasse essa variável com a lista vazia e depois adicionasse todos os seus elementos dentro dela, o resultado 
do min e max seria sempre o último número. Como se apenas o último valor do loop é contado.

    Para adicionar todos os elementos dentro da lista, eu usei += que é como se fosse uma concatenação, uma junção. 
Semelhante aos exercícios anteriores '''
